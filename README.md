# CloudTools

CloudTools - Example Python Cloud Tools template using Typer/Fastapi

```
# CLI
python3 -m venv tempEnv
source tempEnv/bin/activate
pip install -r requirements.txt

# Usage
# python3 ct.py aws list-ec2
# python3 ct.py aws list-rds
# python3 ct.py aws update-r53 
# python3 ct.py gcp list-inst --verbose
# python3 ct.py endpoint-check-all --verbose

# API
bash start_api.sh
```

CLI: https://github.com/tiangolo/typer

API: https://github.com/tiangolo/fastapi
