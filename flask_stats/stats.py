import subprocess
import json
import os
from flask_stats.APIclient import APIclient
from pathlib import Path
from pprint import pprint
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('stats', __name__, url_prefix='/')

@bp.route('/')
def stats():
    client = APIclient()
    sections_part_1 = []
    sections_part_2 = []
    stat_types_1 = ['total_deposits', 'avg_views', 'avg_downloads']
    stat_types_2 = ['top_views', 'top_downloads']
    freqs = ['monthly', 'weekly', 'daily']
    path = Path(__file__).resolve().parent
    stats_CLI_path = str(os.path.join(path, "stats_CLI.py"))

    for stat_type in stat_types_1:
        section = {}
        table_headings = []
        table_entries = []
        # send command line request to get total no. of deposits
        if stat_type == 'total_deposits':
            """ get_stat = subprocess.Popen(["pipenv", "run", "python3", stats_CLI_path, stat_type, "--json-output"], 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True,) """
            total_deposits = client.num_deposits()
        else:
            get_stat = subprocess.Popen(["pipenv", "run", "python3", stats_CLI_path, stat_type, "all", "--json-output"], 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True,)
        stdout_stat, stderr_stat = get_stat.communicate()

        # print(get_stat.returncode)

        pprint(stdout_stat)
        pprint(stderr_stat)

        dict_response = json.loads(stdout_stat)

        section['main_heading'] = dict_response['title']
        section['main_stat'] = dict_response['stat']
        section['table_name'] = section['main_heading'].replace('currently', '')

        for freq in freqs:
            if stat_type == 'total_deposits':
                get_no_deposits_time = subprocess.Popen(["pipenv", "run", "python3", stats_CLI_path, stat_type, freq, "--latest", "--json-output"], 
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            universal_newlines=True,)
            else:
                get_no_deposits_time = subprocess.Popen(["pipenv", "run", "python3", stats_CLI_path, stat_type, "all", freq, "--latest", "--json-output"], 
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            universal_newlines=True,)
            stdout_table, stderr_table = get_no_deposits_time.communicate()
            # pprint(stdout_table)
            # pprint(stderr_table)
            dict_response = json.loads(stdout_table)
            table_headings.append(dict_response['title'])
            #print(dict_response['title'])
            table_entries.append(dict_response['stat'])
            #print(dict_response['stat'])
        
        section['table_headings'] = table_headings
        section['table_entries'] = table_entries

        sections_part_1.append(section)

    for stat_type in stat_types_2:
        section = {}
        table_headings = []
        table_entries = []
        num = '100'

        get_top_deposits = subprocess.Popen(["pipenv", "run", "python3", stats_CLI_path, stat_type, num], 
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            universal_newlines=True,)
        stdout_top, stderr_top = get_top_deposits.communicate()
        table_entries = json.loads(stdout_top)

        if stat_type == "top_views":
            section['main_heading'] = "Statistics for the top 100 deposits (by # of views)"
        else:
            section['main_heading'] = "Statistics for the top 100 deposits (by # of downloads)"
        
        section['table_headings'] = ["No. of views (current version)", "No. of unique views (current version)", "No. of downloads (current version)", 
                                     "No. of unique downloads (current version)"]
        section['table_entries'] = table_entries

        sections_part_2.append(section)

    return render_template('base.html', sections_part_1=sections_part_1, sections_part_2=sections_part_2)