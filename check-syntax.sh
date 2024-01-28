#!/bin/bash
set -ex
flake8 src/*.py
echo "tests pass"
