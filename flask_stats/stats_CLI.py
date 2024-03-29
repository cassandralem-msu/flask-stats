import click
import json
from flask_stats.APIclient import APIclient
from collections import OrderedDict
import os

token = os.environ['CLI_TOKEN']

@click.group()
def cli():
    pass

@cli.command(name='total_deposits')
@click.argument('freq', default=None, required=False)
@click.option('--latest', is_flag=True, required=False)
@click.option('--json-output', is_flag=True, required=False)
def request_total_deposits(freq, latest, json_output):
    client = APIclient(token)
    no_deposits = client.num_deposits(freq, latest)
    if json_output:
        if freq == None:
            click.echo(json.dumps({'title': 'Total number of deposits currently', 'stat': no_deposits}))
        else:
            if latest:
                click.echo(json.dumps({'stat_type': 'Total number of deposits', 
                                       'title': ('today' if freq == "daily" else 'this ' + freq.replace('ly', '')) \
                                       + ' (' + no_deposits['time'] + ')', 
                                       'stat': no_deposits['stat']}))
            else:
                click.echo(json.dumps({'title': 'Total number of deposits ' + freq, 'stat': no_deposits}))
    else:
        if freq == None:
            click.echo(f"Total number of deposits: {no_deposits}!")
        else:
            click.echo(f"Total number of deposits {freq}:")
            for key in no_deposits:
                click.echo(f"{key}: {no_deposits[key]}")


@cli.command(name='num_views')
@click.argument('id', default='all')
@click.argument('version', default='current', required=False)   # options: current or all
@click.argument('start_date', default=None, required=False)      # if a freq option is specified, can only have start 
                                                                    # and end dates within the same calendar year
@click.argument('end_date', default=None, required=False)
@click.argument('freq', default=None, required=False)          # options: monthly, weekly, daily
@click.option('--unique/--not-unique', default=False, required=False)
@click.option('--json-output', is_flag=True, required=False)
def request_num_views(id, version, start_date, end_date, freq, unique, json_output):
    client = APIclient(token)
    no_views = client.num_views(id, version, start_date, end_date, freq, unique)
    if id.lower() == 'all':
        if json_output:
            click.echo(json.dumps({"Total number of " + ("unique" if unique else "") + " views by deposit " 
                                + ("(current versions)" if version.lower() == "current" else "(all versions)"): no_views}))
        else:
            click.echo("Total number of " + ("unique " if unique else "") + "views of " 
                       + ("current version" if version.lower() == "current" else "all versions") + " of each deposit:")
            for key in no_views:
                click.echo(f"Deposit {key}: {no_views[key]}")
    else:
        if json_output:
            if start_date is None and end_date is None:
                click.echo(json.dumps({"Total number of " + ("unique " if unique else "") + "views of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)"): no_views}))
            elif freq != None:
                click.echo(json.dumps({"Numbers of " + ("unique " if unique else "") + freq + " views of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)")
                                + " from " + start_date + " to " + end_date: no_views}))
            else:
                click.echo(json.dumps({"Total number of " + ("unique " if unique else "") + "views of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)") 
                                + " from " + start_date + " to " + end_date: no_views}))
        else:
            if start_date is None and end_date is None:
                click.echo("Total number of " + ("unique " if unique else "") + f"views of deposit {id} " + 
                       ("(current version): " if version.lower() == "current" else "(all versions): ") + f"{no_views}!")
            elif freq != None:
                click.echo("Numbers of " + ("unique " if unique else "") + freq + f" views of deposit {id} " + 
                       ("(current version)" if version.lower() == "current" else "(all versions)") + " from " 
                       + start_date + " to " + end_date + ":")
                for key in no_views:
                    click.echo(str(key) + ": " + str(no_views[key]))
            else:
                click.echo("Total number of " + ("unique " if unique else "") + f"views of deposit {id} " + 
                       ("(current version)" if version.lower() == "current" else "(all versions)") + " from " 
                       + start_date + " to " + end_date + f": {no_views}!")


@cli.command(name='avg_views')
@click.argument('version', default='all', required=False)
@click.argument('freq', default=None, required=False)
@click.argument('start_date', default=None, required=False)
@click.argument('end_date', default=None, required=False)
@click.option('--latest', is_flag=True, required=False)
@click.option('--unique/--not-unique', default=False)
@click.option('--json-output', is_flag=True, required=False)
def request_avg_views(version, freq, start_date, end_date, latest, unique, json_output):
    client = APIclient(token)
    avg = client.avg_views(version, freq, start_date, end_date, latest, unique)
    if freq is None:
        if json_output:
            # click.echo(json.dumps({"Average number of " + ("unique " if unique else "") + "views per deposit, taken from " 
                                # + ("current versions" if version == "current" else "all versions")
                                # + (" over " + start_date + " to " + end_date if start_date != None and end_date != None else ""): avg}))
            click.echo(json.dumps({'title': avg['title'], 'stat': avg['stat']}))
        else:
            click.echo("Average number of " + ("unique " if unique else "") + "views per deposit, taken from "
                    + ("current versions" if version == "current" else "all versions") 
                    + (" over " + start_date + " to " + end_date if start_date != None and end_date != None else "") + f": {avg}")
    
    elif freq != None and start_date != None and end_date != None:
        if json_output:
            click.echo(json.dumps({"Average " + freq + ("unique " if unique else "") + "views per deposit, taken from " 
                                + ("current versions" if version.lower() == "current" else "all versions")
                                + " over " + start_date + " to " + end_date: avg}))
        else:
            click.echo("Average " + freq + " numbers of " + ("unique " if unique else "") + "views per deposit, taken from " 
                        + ("current versions" if version.lower() == "current" else "all versions") + " over " 
                        + start_date + " to " + end_date + ":")
            for key in avg:
                click.echo(str(key) + ": " + str(avg[key]))
    
    elif freq != None and latest:
        if json_output:
            click.echo(json.dumps({'stat_type': 'Average views per deposit', 
                                       'title': 'today ' if freq == 'daily' else 'this ' + freq.replace('ly', '') \
                                       + ' (' + avg['time'] + ')', 
                                       'stat': avg['stat']}))
            


@cli.command(name='num_downloads')
@click.argument('id', default='all')
@click.argument('version', default='current', required=False)
@click.argument('start_date', default=None, required=False)
@click.argument('end_date', default=None, required=False)
@click.argument('freq', default=None, required=False)          # options: monthly, weekly, daily
@click.option('--unique/--not-unique', default=False, required=False)
@click.option('--json-output', is_flag=True, required=False)
def request_num_downloads(id, version, start_date, end_date, freq, unique, json_output):
    client = APIclient(token)
    no_downloads = client.num_downloads(id, version, start_date, end_date, freq, unique)
    if id.lower() == 'all':
        if json_output:
            click.echo(json.dumps({"Total number of " + ("unique" if unique else "") + " downloads by deposit " 
                                + ("(current versions)" if version.lower() == "current" else "(all versions)"): no_downloads}))
        else:
            click.echo("Total number of " + ("unique " if unique else "") + "downloads of " 
                       + ("current version" if version.lower() == "current" else "all versions") + " of each deposit:")
            for key in no_downloads:
                click.echo(f"Deposit {key}: {no_downloads[key]}")
    else:
        if json_output:
            if start_date is None and end_date is None:
                click.echo(json.dumps({"Total number of " + ("unique " if unique else "") + "downloads of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)"): no_downloads}))
            elif freq != None:
                click.echo(json.dumps({"Numbers of " + ("unique " if unique else "") + freq + " downloads of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)")
                                + " from " + start_date + " to " + end_date: no_downloads}))
            else:
                click.echo(json.dumps({"Total number of " + ("unique " if unique else "") + "downloads of deposit " 
                                + id + (" (current version)" if version.lower() == "current" else " (all versions)") 
                                + " from " + start_date + " to " + end_date: no_downloads}))
        else:
            if start_date is None and end_date is None:
                click.echo("Total number of " + ("unique " if unique else "") + f"downloads of deposit {id} " + 
                       ("(current version): " if version.lower() == "current" else "(all versions): ") + f"{no_downloads}!")
            elif freq != None:
                click.echo("Numbers of " + ("unique " if unique else "") + freq + f" downloads of deposit {id} " + 
                       ("(current version)" if version.lower() == "current" else "(all versions)") + " from " 
                       + start_date + " to " + end_date + ":")
                for key in no_downloads:
                    click.echo(str(key) + ": " + str(no_downloads[key]))
            else:
                click.echo("Total number of " + ("unique " if unique else "") + f"downloads of deposit {id} " + 
                       ("(current version)" if version.lower() == "current" else "(all versions)") + " from " 
                       + start_date + " to " + end_date + f": {no_downloads}!")


@cli.command(name='avg_downloads')
@click.argument('version', default='all', required=False)
@click.argument('freq', default=None, required=False)
@click.argument('start_date', default=None, required=False)
@click.argument('end_date', default=None, required=False)
@click.option('--latest', is_flag=True, required=False)
@click.option('--unique/--not-unique', default=False)
@click.option('--json-output', is_flag=True, required=False)
def request_avg_downloads(version, freq, start_date, end_date, latest, unique, json_output):
    client = APIclient(token)
    avg = client.avg_downloads(version, freq, start_date, end_date, latest, unique)
    if freq is None:
        if json_output:
            # click.echo(json.dumps({"Average number of " + ("unique " if unique else "") + "downloads per deposit, taken from " 
                                # + ("current version" if version == "current" else "all versions")
                                # + (" over " + start_date + " to " + end_date if start_date != None and end_date != None else ""): avg}))
            click.echo(json.dumps({'title': avg['title'], 'stat': avg['stat']}))
        else:
            click.echo("Average number of " + ("unique " if unique else "") + "downloads per deposit, taken from "
                    + ("current versions" if version == "current" else "all versions") 
                    + (" over " + start_date + " to " + end_date if start_date != None and end_date != None else "") + f": {avg}")
    
    elif freq != None and start_date != None and end_date != None:
        if json_output:
            click.echo(json.dumps({"Average " + freq + ("unique " if unique else "") + "downloads per deposit, taken from " 
                                + ("current versions" if version.lower() == "current" else "all versions")
                                + " over " + start_date + " to " + end_date: avg}))
        else:
            click.echo("Average " + freq + " numbers of " + ("unique " if unique else "") + "downloads per deposit, taken from " 
                        + ("current versions" if version.lower() == "current" else "all versions") + " over " 
                        + start_date + " to " + end_date + ":")
            for key in avg:
                click.echo(str(key) + ": " + str(avg[key]))

    elif freq != None and latest:
        if json_output:
            click.echo(json.dumps({'stat_type': 'Average downloads per deposit', 
                                       'title': 'today ' if freq == 'daily' else 'this ' + freq.replace('ly', '') \
                                       + ' (' + avg['time'] + ')', 
                                       'stat': avg['stat']}))


@cli.command(name='top_views')
@click.argument('num', default='100')
def request_top_views(num):
    client = APIclient(token)
    sorted_views = client.top_views(int(num))
    top_deposits_views = OrderedDict()
    for id in sorted_views:
        no_views = sorted_views[id]['stats']['this_version']['views']
        no_unique_views = sorted_views[id]['stats']['this_version']['unique_views']
        no_downloads = sorted_views[id]['stats']['this_version']['downloads']
        no_unique_downloads = sorted_views[id]['stats']['this_version']['unique_downloads']
        top_deposits_views[id] = [no_views, no_unique_views, no_downloads, no_unique_downloads]
    click.echo(json.dumps(top_deposits_views))

    """
    click.echo(f"Top {num} deposits by number of views:")
    index = -1
    for i in range(0, num):
        key = list(sorted_views)[index]
        click.echo(f"Deposit {key}: {sorted_views[key]} views")
        index += 1
    """

@cli.command(name='top_downloads')
@click.argument('num', default='100')
def request_top_downloads(num):
    client = APIclient(token)
    sorted_downloads = client.top_downloads(int(num))
    top_deposits_downloads = OrderedDict()
    for id in sorted_downloads:
        no_views = sorted_downloads[id]['stats']['this_version']['views']
        no_unique_views = sorted_downloads[id]['stats']['this_version']['unique_views']
        no_downloads = sorted_downloads[id]['stats']['this_version']['downloads']
        no_unique_downloads = sorted_downloads[id]['stats']['this_version']['unique_downloads']
        top_deposits_downloads[id] = [no_views, no_unique_views, no_downloads, no_unique_downloads]
    click.echo(json.dumps(top_deposits_downloads))
    
    """
    click.echo(f"Top {num} deposits by number of downloads:")
    index = -1
    for i in range(0, num):
        key = list(sorted_downloads)[index]
        click.echo(f"Deposit {key}: {sorted_downloads[key]} downloads")
        index += 1
    """


if __name__ == '__main__':
    cli()