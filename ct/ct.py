import typer
import requests
import pprint

# Usage
# python3 ct.py aws list-inst
# python3 ct.py gcp list-inst --verbose
# python3 ct.py endpoint-check http://www.chrisgr.com --verbose

app = typer.Typer()


@app.command()
def aws(cmd: str, verbose: bool = False):
    """ AWS cmd """
    typer.echo(f"AWS cmd {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    if cmd == "list-inst":
        typer.echo(f"Run AWS cmd {cmd}")
    elif cmd == "list_rds":
        typer.echo(f"Run AWS cmd {cmd}")
    else:
        typer.echo(f"Run AWS cmd {cmd}")



@app.command()
def gcp(cmd: str, verbose: bool = False):
    """ GCP cmd """
    typer.echo(f"GCP cmd {cmd}")
    if verbose:
        typer.echo(f"Verbose on")
    if cmd == "list-inst":
        typer.echo(f"Run GCP cmd {cmd}")
    else:
        typer.echo(f"Run GPC cmd {cmd}")


@app.command()
def endpoint_check(url: str, verbose: bool = False):
    """ Endpoint check """
    typer.echo(f"Endpoint check {url}")
    if verbose:
        typer.echo(f"Verbose on")
    response = requests.get(url)
    if response.status_code == 200:
        print("200 ok")
    if verbose:
        pprint.pprint(response.content)
        pprint.pprint(response.text)

if __name__ == "__main__":
    app()
