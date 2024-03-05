import subprocess
import json
from pprint import pprint
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('stats', __name__, url_prefix='/')

@bp.route('/')
def stats():
    sections = []
    stat_types = ['total_deposits', 'avg_views', 'avg_downloads']
    freqs = ['monthly', 'weekly', 'daily']

    for stat_type in stat_types:
        section = {}
        table_headings = []
        table_entries = []
        # send command line request to get total no. of deposits
        if stat_type == 'total_deposits':
            get_stat = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", stat_type, "--json-output"], 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True,)
        else:
            get_stat = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", stat_type, "all", "--json-output"], 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True,)
        stdout_stat, stderr_stat = get_stat.communicate()

        # print(get_stat.returncode)

        pprint(stdout_stat)
        # pprint(stderr_stat)

        dict_response = json.loads(stdout_stat)

        section['main_heading'] = dict_response['title']
        section['main_stat'] = dict_response['stat']
        section['table_name'] = section['main_heading'].replace('currently', '')

        for freq in freqs:
            if stat_type == 'total_deposits':
                get_no_deposits_time = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", stat_type, freq, "--latest", "--json-output"], 
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            universal_newlines=True,)
            else:
                get_no_deposits_time = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", stat_type, "all", freq, "--latest", "--json-output"], 
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            universal_newlines=True,)
            stdout_table, stderr_table = get_no_deposits_time.communicate()
            pprint(stdout_table)
            dict_response = json.loads(stdout_table)
            table_headings.append(dict_response['title'])
            #print(dict_response['title'])
            table_entries.append(dict_response['stat'])
            #print(dict_response['stat'])
        
        section['table_headings'] = table_headings
        section['table_entries'] = table_entries

        sections.append(section)

    return render_template('base.html', sections=sections)