#!/usr/bin/env python3

# Usage
# python3 ct.py aws list-inst
# python3 ct.py gcp list-inst --verbose
# python3 ct.py endpoint-check-all --verbose

import typer
import requests
import pprint

import ct_lib as ct_lib
import ct_inv as ct_inv

app = typer.Typer()


@app.command()
def aws(cmd: str, verbose: bool = False):
    """ AWS cmd """
    typer.echo(f"AWS cmd {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    ct_lib.ask_continue()
    if cmd == "list-inst":
        typer.echo(f"Run AWS cmd {cmd}")
        ct_lib.aws_list_inst()
    elif cmd == "list_rds":
        typer.echo(f"Run AWS cmd {cmd}")
    else:
        typer.echo(f"Run AWS cmd {cmd}")


@app.command()
def gcp(cmd: str, verbose: bool = False):
    """ GCP cmd """
    typer.echo(f"GCP cmd {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    if cmd == "list-inst":
        typer.echo(f"Run GCP cmd {cmd}")

    else:
        typer.echo(f"Run GPC cmd {cmd}")


@app.command()
def endpoint_check_all(verbose: bool = False):
    """ Endpoint check """
    if verbose:
        typer.echo(f"Verbose on")
        pprint.pprint(ct_inv.server_list)
    for url in ct_inv.server_list:
        typer.echo(f"Endpoint check {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print("200 ok")
        if verbose:
            pprint.pprint(response.content)
            pprint.pprint(response.text)
            pprint.pprint(response.headers)


if __name__ == "__main__":
    app()
