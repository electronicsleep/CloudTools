# CloudTools

CloudTools - Python Cloud Tools using Typer/FastAPI/Rust

Example demonstrating a Python package command line interface
- Unified cloud command line cmd example using Typer
- Automatic documentation creation
- Linting using Ruff and PEP8
- Simple api using FastAPI
- Rust integration

### Python virtualenv
```
brew install virtualenv
virtualenv tempEnv
source tempEnv/bin/activate
pip3 install -r requirements.txt
```

### Python Dev
```
make
make test
make install
```

### Python Dev
```
python3 src/ct.py --help
python3 src/ct.py cs
python3 src/ct.py aws -c li
python3 src/ct.py gcp -c li
```

### API
```
pip3 install -r requirements_api.txt
bash api.sh
bash src/test/curl-tests.sh

# Swagger
http://127.0.0.1:8081/docs
```

### Python3/Rust

For things that need to run faster/safer

Building will enable Rust Python Functions
```
bash build.sh
python3 src/ct.py rust-version
python3 src/ct.py rust-print -c hello
python3 src/ct.py rust-rand -c hello
```

### Python Package
```
pip3 install .

ct --help
ct cs
ct aws -c li
ct gcp -c li

# For Rust
# Find where ct is installed
pip3 show ct | grep Location
# Example: Copy to site-packages dir
cp src/libcloudtools.so $(pip3 show ct | grep Location | tail -n1 | cut -f2 -d:)
make docs
```

### Uninstall Python Package
```
pip3 uninstall ct
```


### Links

Python: https://www.python.org

Typer: https://github.com/tiangolo/typer

FastAPI: https://github.com/tiangolo/fastapi

Rust: https://www.rust-lang.org

Rust cpython: https://crates.io/crates/cpython
