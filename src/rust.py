#!/usr/bin/env python3
# Python calling Rust cpython library
# Build: cd lib && bash build.sh
import lib.libcloudtools as libcloudtools 

name = input("what is your name?\n")

result = libcloudtools.get_version()
print(result)

result = libcloudtools.get_result(f"get_result: Rust Name: {name}")
print(result)

result = libcloudtools.run_get_test(f"run_get_test: Rust: Name: {name}")
print(result)
