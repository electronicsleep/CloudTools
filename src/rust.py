#!/usr/bin/env python3
# Python calling Rust cpython library
# Build: cd lib && bash build.sh
import lib.libcloudtools as libcloudtools 

result = libcloudtools.get_version()
print(result)

result = libcloudtools.get_result("get_result: Rust")
print(result)

result = libcloudtools.run_get_test("run_get_test: Rust")
print(result)
