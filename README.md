# CloudTools

CloudTools - Python Cloud Tools using Typer/Fastapi/Rust

### Python Dev
```
pip3 install -r requirements.txt

python3 src/ct.py --help
python3 src/ct.py cs
python3 src/ct.py aws -c li
python3 src/ct.py gcp -c li
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

### API
```
pip3 install -r requirements_api.txt
bash run_api.sh
bash src/test/curl-tests.sh

# Swagger
http://127.0.0.1:8080/docs
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
cp libcloudtools.so /usr/local/lib/python3.9/site-packages/
```

### Uninstall Python Package
```
pip3 uninstall ct
```

### Venv
```
python3 -m venv tempEnv
source tempEnv/bin/activate
pip3 install -r requirements.txt

cd src
python3 ct.py --help
python3 ct.py aws -c li
```

### Versions Tested

MacOS Monterey

Python 3.10.8 pip 22.2.2

MacOS Big Sur

Python 3.9.13 pip 22.1.1

Ubuntu 20.04.4 LTS

Ubuntu 22.04.4 LTS

Python 3.8.10 pip 20.0.2

### Links

Python: https://www.python.org

Typer: https://github.com/tiangolo/typer

FastAPI: https://github.com/tiangolo/fastapi

Rust: https://www.rust-lang.org

Rust cpython: https://crates.io/crates/cpython
