# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Python Package
```
pip3 install -r requirements.txt
pip3 install .

ct --help
ct aws --help
ct aws -c list-ec2
ct aws -c list-rds
ct aws -c update-r53

ct gcp --help
ct gcp -c list-inst --verbose
ct check-sites --verbose
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
