#!/bin/bash
set -ex
URL=http://127.0.0.1:8081
curl --fail $URL/
echo "-"
curl --fail $URL/api
echo "-"
curl --fail $URL/health
echo "-"
curl --fail $URL/items/123
echo "Tests Pass"
