#!/usr/bin/env python3
# Purpose: Test Python calling Rust cpython library

import libcloudtools
import typer


def main(cmd: str = typer.Argument("hello"),
         verbose: bool = typer.Option(False, "--verbose", "-v")):
    """ Rust """
    typer.echo(f"Rust cmd: {cmd} verbose: {verbose}")

    print("Rust Version")
    result = libcloudtools.rust_version()
    print(result)

    print("Rust Print")
    result = libcloudtools.rust_print(f"rust_print: Rust Cmd: {cmd}")
    print(result)

    print("Rust Rand")
    result = libcloudtools.rust_rand(f"rust_rand: Rust: Cmd: {cmd}")
    print(result)


if __name__ == "__main__":
    typer.run(main)
