# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Setup
```
pip3 install -r requirements.txt
pip3 install .

ct --help
ct aws list-ec2
ct aws list-rds
ct aws update-r53
ct gcp list-inst --verbose
ct endpoint-check-all --verbose
```

API
```
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
python3 ct.py aws list-ec2
```

CLI: https://github.com/tiangolo/typer


API: https://github.com/tiangolo/fastapi
