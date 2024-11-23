#!/bin/bash
set -e
flake8 src/*.py
echo "Flake8 checks passed"
ruff check
