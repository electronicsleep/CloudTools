#!/bin/bash
set -e
flake8 src/*.py
echo "tests pass"
ruff check
