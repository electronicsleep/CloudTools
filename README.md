# CloudTools

CloudTools - Python Cloud Tools template using Typer/Fastapi

Setup Module
```
python3 setup.py develop
```

CLI
```
python3 -m venv tempEnv
source tempEnv/bin/activate
pip install -r requirements.txt
cd src

# Usage
# python3 ct.py aws list-ec2
# python3 ct.py aws list-rds
# python3 ct.py aws update-r53 
# python3 ct.py gcp list-inst --verbose
# python3 ct.py endpoint-check-all --verbose

```

API
```
bash start_api.sh

curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/api
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/items/123

# Swagger
curl http://127.0.0.1:8000/docs
```

CLI: https://github.com/tiangolo/typer


API: https://github.com/tiangolo/fastapi
