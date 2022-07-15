#!/usr/bin/env python3
# Python calling Rust cpython library
# Build: cd lib && bash build.sh
import lib.libcloudtools as libcloudtools 

import typer

def main(cmd: str = typer.Argument("hello"), verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Rust """
    typer.echo(f"Rust cmd: {cmd} verbose: {verbose}")

    result = libcloudtools.get_version()
    print(result)

    result = libcloudtools.get_result(f"get_result: Rust Cmd: {cmd}")
    print(result)

    result = libcloudtools.run_get_test(f"run_get_test: Rust: Cmd: {cmd}")
    print(result)


if __name__ == "__main__":
    typer.run(main)
