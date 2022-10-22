# CloudTools

CloudTools - Python Cloud Tools project using Typer/Fastapi

Idea is to keep commands short and consistent use list-inst for aws/gcp

CloudTools uses Python packaging to install the command in the users path

### Python Dev
```
pip3 install -r requirements.txt

cd src
python3 ct.py --help
python3 ct.py cs
python3 ct.py aws -c list-inst
python3 ct.py gcp -c list-inst
```

### Python3/Rust

For things that need to run faster/safer

Building will enable Rust Python Functions
```
./build.sh
cd src
python3 ct.py rust-version
python3 ct.py rust-print -c hello
python3 ct.py rust-rand -c hello
```

### API
```
pip3 install -r requirements_api.txt
bash start_api.sh

bash src/test/curl-tests.sh

# Swagger
http://127.0.0.1:8080/docs
```

### Python Package
```
pip3 install .

ct --help
ct cs
ct aws -c list-inst
ct gcp -c list-inst

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
python3 ct.py aws -c list-inst
```

### Versions Tested

MacOS Big Sur

Python 3.9.13 pip 22.1.1

Ubuntu 20.04.4 LTS

Python 3.8.10 pip 20.0.2

### Links

Python: https://www.python.org

Typer: https://github.com/tiangolo/typer

FastAPI: https://github.com/tiangolo/fastapi

Rust: https://www.rust-lang.org

Rust cpython: https://crates.io/crates/cpython
