#!/bin/bash
# Build and move Rust cpython library
# https://docs.rs/cpython/latest/cpython
set -e
cargo rustc --release -- -C link-arg=-undefined -C link-arg=dynamic_lookup
cp target/release/libcloudtools.dylib ./libcloudtools.so
echo "build ok"
cd ../
python3 rust.py
echo "ran rust.py ok"
