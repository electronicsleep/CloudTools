#!/bin/bash
# Build/Run Rust cpython library
# https://docs.rs/cpython/latest/cpython
set -x
UNAME=$(uname)

if [[ "$UNAME" == "Linux" ]]; then
  cargo rustc --release
  rm src/libcloudtools.so
  cp target/release/libcloudtools.so src/libcloudtools.so
elif [[ "$UNAME" == "Darwin" ]]; then
  cargo rustc --release -- -C link-arg=-undefined -C link-arg=dynamic_lookup
  rm src/libcloudtools.so
  cp target/release/libcloudtools.dylib src/libcloudtools.so
fi

echo "build ok"
cd src
python3 rust.py hello
echo "python3 rust.py ok"
