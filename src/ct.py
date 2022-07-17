#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 ct.py aws -c list-ec2
# python3 ct.py gcp -c list-inst
# python3 ct.py check-sites

import typer
import requests
import pprint

import ct_lib as ct_lib
import ct_inv as ct_inv

main = typer.Typer()

default_aws_region = 'us-west-1'
default_gcp_project = 'qa'


@main.command()
def aws(cmd: str = typer.Option(..., "--cmd", "-c", help="list-ec2, list-rds, update-r53"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ aws cmd """
    if verbose:
        typer.echo(f"aws cmd: {cmd} verbose: {verbose}")
    if cmd == "list-ec2":
        ct_lib.aws_list_ec2(default_aws_region, verbose)
    elif cmd == "list-rds":
        typer.echo(f"aws cmd: {cmd}")
    elif cmd == "update-r53":
        typer.echo(f"aws cmd {cmd} are you sure you want to update r53?")
        ct_lib.ask_continue()
        ct_lib.aws_update_r53(verbose)


@main.command()
def gcp(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ gcp cmd """
    if verbose:
        typer.echo(f"gcp cmd: {cmd} verbose: {verbose}")
    if cmd == "list-inst":
        ct_lib.gcp_list_inst(default_gcp_project, verbose)
    if cmd == "test-ls":
        ct_lib.test_ls(verbose)


@main.command()
def check_sites(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Endpoint check """
    if verbose:
        typer.echo(f"check_sites: verbose: {verbose}")
        pprint.pprint(ct_inv.server_list)
    for url in ct_inv.server_list:
        typer.echo(f"check_sites cmd: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print("200 ok")
        if verbose:
            pprint.pprint(response.content)
            pprint.pprint(response.text)
            pprint.pprint(response.headers)


if __name__ == "__main__":
    main()
