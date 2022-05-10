#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 ct.py aws list-ec2
# python3 ct.py aws list-rds
# python3 ct.py aws update-r53 
# python3 ct.py gcp list-inst --verbose
# python3 ct.py endpoint-check-all --verbose

import typer
import requests
import pprint

import ct_lib as ct_lib
import ct_inv as ct_inv

main = typer.Typer()


@main.command()
def aws(cmd: str = typer.Option(..., "--cmd", "-c"), verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ AWS cmd """
    typer.echo(f"AWS cmd: {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    if cmd == "list-ec2":
        typer.echo(f"Run AWS cmd: {cmd}")
        ct_lib.aws_list_ec2(verbose)
    elif cmd == "list-rds":
        typer.echo(f"Run AWS cmd: {cmd}")
    elif cmd == "update-r53":
        typer.echo(f"Run AWS cmd: {cmd}")
        typer.echo(f"Are you sure you want to update r53?")
        ct_lib.ask_continue()
        ct_lib.aws_update_r53(verbose)
    else:
        typer.echo(f"Cmd not defined: {cmd}")


@main.command()
def gcp(cmd: str = typer.Option(..., "--cmd", "-c"), verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ GCP cmd """
    typer.echo(f"GCP cmd: {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    if cmd == "list-inst":
        typer.echo(f"Run GCP cmd: {cmd}")

    else:
        typer.echo(f"Cmd not defined: {cmd}")


@main.command()
def check_sites(verbose: bool = typer.Option(False, "--verbose", "-v")):
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
    main()
