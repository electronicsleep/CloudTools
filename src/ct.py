#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 ct.py --help
# python3 ct.py aws -c li
# python3 ct.py gcp -c li
# python3 ct.py cs

import typer
from rich import print
import platform
import ct_lib as ct_lib
import ct_inv as ct_inv
from importlib.metadata import version
from pkg_resources import get_distribution


try:
    if platform.system() == "Darwin":
        __version__ = version('ct')
    else:
        __version__ = get_distribution('ct').version
except Exception as e:
    __version__ = "0.0.0"
    print(f"INFO: Python package not installed try: 'pip3 install .'")
    if verbose:
        print(f"INFO {e}")


rust_support = False
try:
    import ct_rust as ct_rust
    rust_support = True
except ModuleNotFoundError as e:
    print(f"Rust cpython library not built skip\nINFO: {e}")
    pass

main = typer.Typer()

default_aws_region = "us-west-1"
default_gcp_project = "qa"


def version_callback(value: bool):
    if value:
        print(f"CloudTools (ct) version: {__version__}")
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
def aws(cmd: str = typer.Option("li", "--cmd", "-c", help="commands: li, ldb, udns"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ aws cmd: default: li """
    print(f"[bold red]aws_cmd: {cmd}[/bold red]")
    if cmd == "ldb":
        print(f"aws_cmd: {cmd} run ldb")
        if verbose:
            print(f"aws_cmd: {cmd} verbose on: {verbose}")
    elif cmd == "r53":
        print(f"aws_cmd: {cmd} update r53?")
        ct_lib.ask_continue()
        ct_lib.aws_udns(verbose)
    else:
        print("aws_cmd: li")
        ct_lib.aws_li(default_aws_region, verbose)


@main.command()
def gcp(cmd: str = typer.Option("li", "--cmd", "-c", help="commands: li"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ gcp cmd: default: li """
    print("[bold red]gcp_cmd[/bold red]")
    if verbose:
        print(f"gcp_cmd: {cmd} verbose: {verbose}")
    else:
        print("[bold red]gcp_cmd: li[/bold red]")
        ct_lib.gcp_li(default_gcp_project, verbose)


if rust_support:

    @main.command()
    def rust_version():
        """ Rust Version """
        print(f"[bold red]rust_version:[/bold red]")
        ct_rust.rust_version()

    @main.command()
    def rust_print(cmd: str = typer.Option(..., "--cmd", "-c", help="ls"),
                   verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Print """
        print(f"[bold red]rust_print: {cmd}[/bold red]")
        ct_rust.rust_print(cmd, verbose)

    @main.command()
    def rust_rand(cmd: str = typer.Option(..., "--cmd", "-c", help="ls"),
                  verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Rand """
        ct_rust.rust_rand(cmd, verbose)


if __name__ == "__main__":
    main()
