#!/bin/bash
set -ex
curl --fail http://127.0.0.1:8080/
echo "-"
curl --fail http://127.0.0.1:8080/api
echo "-"
curl --fail http://127.0.0.1:8080/health
echo "-"
curl --fail http://127.0.0.1:8080/items/123
echo "Tests Pass"
