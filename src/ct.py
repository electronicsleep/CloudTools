#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 ct.py --help
# python3 ct.py aws -c list-ec2
# python3 ct.py gcp -c list-inst
# python3 ct.py cs

import typer
from rich import print
import ct_lib as ct_lib
import ct_inv as ct_inv
from pkg_resources import get_distribution

#__version__ = get_distribution('ct').version
__version__ = "0.3.1"

rust_support = False
try:
    import ct_rust as ct_rust
    rust_support = True
except ModuleNotFoundError as e:
    print(f"Rust cpython library not built skip\n-> {e}")
    pass

main = typer.Typer()

default_aws_region = 'us-west-1'
default_gcp_project = 'qa'


def version_callback(value: bool):
    if value:
        print(f"CloudTools (ct) Version: {__version__}")
        raise typer.Exit()


@main.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass


@main.command()
def cs(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Endpoint Check: Check Sites """
    print("[bold red]check_sites[/bold red]")
    ct_lib.check_sites(ct_inv.server_list, verbose)


@main.command()
def test():
    """ Test cmd """
    print("[bold red]test[/bold red]")
    ct_lib.ask_continue()


@main.command()
def aws(cmd: str = typer.Option("list-inst", "--cmd", "-c", help="list-inst, list-rds, update-r53"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ aws sub cmd: default: list-inst """
    if verbose:
        print(f"aws cmd: {cmd} verbose: {verbose}")
    if cmd == "list-rds":
        print(f"aws cmd: {cmd}")
    elif cmd == "update-r53":
        print(f"aws cmd {cmd} are you sure you want to update r53?")
        ct_lib.ask_continue()
        ct_lib.aws_update_r53(verbose)
    else:
        print("using default list-inst")
        ct_lib.aws_list_inst(default_aws_region, verbose)


@main.command()
def gcp(cmd: str = typer.Option("list-inst", "--cmd", "-c", help="list-inst"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ gcp sub cmd """
    if verbose:
        print(f"gcp cmd: {cmd} verbose: {verbose}")
    if cmd == "list-inst":
        ct_lib.gcp_list_inst(default_gcp_project, verbose)
    else:
        print("using default list-inst")
        ct_lib.gcp_list_inst(default_gcp_project, verbose)


if rust_support:

    @main.command()
    def rust_version():
        """ Rust Version """
        print(f"[bold red]rust_version:[/bold red]")
        ct_rust.rust_version()

    @main.command()
    def rust_print(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
                   verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Print """
        print(f"[bold red]rust_print: {cmd}[/bold red]")
        ct_rust.rust_print(cmd, verbose)

    @main.command()
    def rust_rand(cmd: str = typer.Option(..., "--cmd", "-c", help="list-inst"),
                  verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Rand """
        ct_rust.rust_rand(cmd, verbose)


if __name__ == "__main__":
    main()
