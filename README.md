# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Python
```
pip3 install -r requirements.txt

cd src
python3 ct.py aws -c list-ec2
python3 ct.py gcp -c list-inst
python3 ct.py check-sites -v
```

Python Package
```
pip3 install .

ct aws -c list-ec2
ct gcp -c list-inst
ct check-sites -v
```

Uninstall Python Package
```
pip3 uninstall ct
```

API
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

VENV
```
python3 -m venv tempEnv
source tempEnv/bin/activate
pip3 install -r requirements.txt

cd src
python3 ct.py --help
python3 ct.py aws -c list-ec2
```

Python3/Rust
```
cd src/lib && bash build.sh
python3 rust.py
```

Python: https://www.python.org

Typer: https://github.com/tiangolo/typer

FastAPI: https://github.com/tiangolo/fastapi

Rust: https://www.rust-lang.org

Rust cPython: https://crates.io/crates/cpython
