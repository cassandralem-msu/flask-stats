import subprocess
import json
from pprint import pprint
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('stats', __name__, url_prefix='/')

@bp.route('/')
def stats():
    sections = {}
    stat_types = ['total_deposits', 'avg_views', 'avg_downloads']
    freqs = ['monthly', 'weekly', 'daily']


    # send command line request to get total no. of deposits
    get_no_deposits = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", "total_deposits", "--json-output"], 
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True,)
    stdout_gnd, stderr_gnd = get_no_deposits.communicate()

    # print(get_no_deposits.returncode)

    # pprint(stdout_gnd)
    # pprint(stderr_gnd)

    dict_response = json.loads(stdout_gnd)

    for key in dict_response:
        sections[key] = dict_response[key]

    for freq in freqs:
        get_no_deposits_time = subprocess.Popen(["pipenv", "run", "python3", "stats_CLI.py", "total_deposits", freq, "--json-output"], 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True,)
        stdout_gndt, stderr_gndt = get_no_deposits_time.communicate()
        dict_response = json.loads(stdout_gndt)
        for key in dict_response:
            deposit_stats[key] = dict_response[key]

    return render_template('base.html', headings=headings, deposit_stats=deposit_stats)