#!/bin/bash
set -e
DIR=$(dirname "$0")

if [[ "$DIR" == "src/scripts" ]]; then
  echo "OK"
else
  echo "run from the root of the project"
  exit 1
fi

typer src/ct.py utils docs --name ct --output DOCS.md
