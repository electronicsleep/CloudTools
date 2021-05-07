import typer
import requests
import pprint

# Usage
# python3 ct.py aws list-inst
# python3 ct.py gcp list-inst --verbose

app = typer.Typer()


@app.command()
def aws(action: str, verbose: bool = False):
    """ AWS commands using Boto3 """
    if action == "list-inst":
        typer.echo(f"AWS action {action}")
    elif action == "list_rds":
        typer.echo(f"AWS action {action}")
    else:
        typer.echo(f"AWS action {action}")



@app.command()
def gcp(action: str, verbose: bool = False):
    if action == "list-inst":
        typer.echo(f"GCP action {action}")
    else:
        typer.echo(f"GPC action {action}")


if __name__ == "__main__":
    app()
