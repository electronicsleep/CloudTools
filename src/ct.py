#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 ct.py --help
# python3 ct.py aws -c list-ec2
# python3 ct.py gcp -c list-inst
# python3 ct.py cs

import typer
import ct_lib as ct_lib
import ct_inv as ct_inv
try:
    import ct_rust as ct_rust
except Exception as e:
    print(f"Rust cpython library not built skip\n-> {e}")
    pass

main = typer.Typer()

default_aws_region = 'us-west-1'
default_gcp_project = 'qa'


@main.command()
def cs(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Endpoint Check: Check Sites """
    ct_lib.check_sites(ct_inv.server_list, verbose)


@main.command()
def test(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Endpoint Check: Check Sites """
    ct_lib.check_sites(ct_inv.server_list, verbose)


@main.command()
def aws(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst, list-rds, update-r53"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ aws sub cmd: default: list-inst """
    if verbose:
        typer.echo(f"aws cmd: {cmd} verbose: {verbose}")
    if cmd == "list-rds":
        typer.echo(f"aws cmd: {cmd}")
    elif cmd == "update-r53":
        typer.echo(f"aws cmd {cmd} are you sure you want to update r53?")
        ct_lib.ask_continue()
        ct_lib.aws_update_r53(verbose)
    else:
        print("using default list-inst")
        ct_lib.aws_list_inst(default_aws_region, verbose)


@main.command()
def gcp(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ gcp sub cmd """
    if verbose:
        typer.echo(f"gcp cmd: {cmd} verbose: {verbose}")
    if cmd == "list-inst":
        ct_lib.gcp_list_inst(default_gcp_project, verbose)
    else:
        print("using default list-inst")
        ct_lib.gcp_list_inst(default_gcp_project, verbose)


@main.command()
def rust_print(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
               verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Rust Get Result """
    ct_rust.rust_print(cmd, verbose)


@main.command()
def rust_cloud_tools(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
                     verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Rust Cloud Tools """
    ct_rust.rust_cloud_tools(cmd, verbose)


if __name__ == "__main__":
    main()
