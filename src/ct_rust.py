#!/usr/bin/env python3
# Author: Chris Robertson electronicsleep@gmail.com
# Purpose: CloudTools - Python cloud tools template using Typer/Fastapi

import libcloudtools


def rust_print(cmd, verbose):
    print(f"verbose: {verbose}")
    result = libcloudtools.rust_print(f"rust_print: cmd: {cmd}")
    print(f"result: {result}")


def rust_rand(cmd, verbose):
    print(f"verbose: {verbose}")
    result = libcloudtools.rust_rand(f"rust_rand: cmd: {cmd}")
    print(f"result: {result}")