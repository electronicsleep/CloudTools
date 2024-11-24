#!/bin/bash
cd src
uvicorn --port 8081 api:app --reload
