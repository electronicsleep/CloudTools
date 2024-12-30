#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

# Usage:
# python3 src/ct.py --help
# python3 src/ct.py aws -c li
# python3 src/ct.py gcp -c li
# python3 src/ct.py kube-events
# python3 src/ct.py cs

import typer
from rich import print as rprint
from importlib.metadata import version
import ct_kube as ct_kube
import ct_lib as ct_lib
import ct_inv as ct_inv

verbose = False

try:
    __version__ = version('ct')
except Exception as e:
    __version__ = "0.0.0"
    if verbose:
        print("INFO: Python package not installed try: 'pip3 install .'")
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
    """Endpoint Check: Check Sites"""
    rprint("[bold blue]check_sites[/bold blue]")
    ct_lib.check_sites(ct_inv.server_list, verbose)


@main.command()
def test():
    """Test cmd"""
    rprint("[bold blue]test[/bold blue]")
    print(ct_lib.date_ymd())


@main.command()
def aws(cmd: str = typer.Option("li", "--cmd", "-c", help="commands: li, ldb, udns"),
        verbose: bool = typer.Option(False, "--verbose", "-v")):
    """AWS cmd: default: li"""
    rprint(f"[bold blue]aws_cmd: {cmd}[/bold blue]")
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
    """GCP cmd: default: li """
    rprint("[bold blue]gcp_cmd[/bold blue]")
    if verbose:
        print(f"gcp_cmd: {cmd} verbose: {verbose}")
    else:
        rprint("[bold blue]gcp_cmd: li[/bold blue]")
        ct_lib.gcp_li(default_gcp_project, verbose)


@main.command()
def kube_events(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """Kube Check"""
    rprint("[bold blue]kube_events[/bold blue]")
    ct_kube.check_events(verbose)


@main.command()
def kube_pods(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """Kube Check"""
    rprint("[bold blue]check_kube[/bold blue]")
    ct_kube.check_pods(verbose)


if rust_support:
    @main.command()
    def rust_version():
        """ Rust Version """
        rprint("[bold blue]rust_version:[/bold blue]")
        ct_rust.rust_version()

    @main.command()
    def rust_print(cmd: str = typer.Option("test", "--cmd", "-c", help="rust_print"),
                   verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Print """
        rprint(f"[bold blue]rust_print: {cmd}[/bold blue]")
        ct_rust.rust_print(cmd, verbose)

    @main.command()
    def rust_rand(cmd: str = typer.Option(..., "--cmd", "-c", help="rust_rand"),
                  verbose: bool = typer.Option(False, "--verbose", "-v")):
        """ Rust Rand """
        ct_rust.rust_rand(cmd, verbose)


if __name__ == "__main__":
    main()
