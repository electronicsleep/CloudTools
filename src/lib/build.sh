#!/bin/bash
# Build/Run Rust cpython library
# https://docs.rs/cpython/latest/cpython
set -e
UNAME=$(uname)

if [[ "$UNAME" == "Linux" ]]; then
  cargo rustc --release
  cp target/release/libcloudtools.so ./libcloudtools.so
else
  cargo rustc --release -- -C link-arg=-undefined -C link-arg=dynamic_lookup
  cp target/release/libcloudtools.dylib ./libcloudtools.so
fi

echo "build ok"
cd ../
python3 rust.py hello
echo "ran rust.py ok"
