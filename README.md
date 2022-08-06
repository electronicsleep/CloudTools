# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Idea is to keep commands short and consistent use list-inst for aws/gcp

### Python Package
```
pip3 install .

ct --help
ct cs
ct aws -c list-inst
ct gcp -c list-inst
```

Uninstall Python Package
```
pip3 uninstall ct
```

### Python Dev
```
pip3 install -r requirements.txt

cd src
python3 ct.py --help
python3 ct.py cs
python3 ct.py aws -c list-inst
python3 ct.py gcp -c list-inst
```

### API
```
pip3 install -r requirements_api.txt
bash start_api.sh

curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/api
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/items/123

# Swagger
http://127.0.0.1:8080/docs
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

### Python3/Rust

For things that need to run faster
```
cd src/lib && bash build.sh
python3 rust.py
```

### Version

Python 3.9.7
pip 22.2

verified working

Python 3.8.10
pip 20.0.2

MacOS Big Sur
Ubuntu 20.04.4 LTS

### Links

Python: https://www.python.org

Typer: https://github.com/tiangolo/typer

FastAPI: https://github.com/tiangolo/fastapi

Rust: https://www.rust-lang.org

Rust cPython: https://crates.io/crates/cpython
