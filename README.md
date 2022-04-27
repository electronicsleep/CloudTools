# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Setup
```
python3 setup.py develop
ct --help

ct aws list-ec2
ct aws list-rds
ct aws update-r53
ct gcp list-inst --verbose
ct endpoint-check-all --verbose
```

VENV
```
cd src
python3 -m venv tempEnv
source tempEnv/bin/activate
pip install -r ../requirements.txt
python3 ct.py --help
python3 ct.py aws list-ec2

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

CLI: https://github.com/tiangolo/typer


API: https://github.com/tiangolo/fastapi
