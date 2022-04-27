#!/bin/bash
cd src
uvicorn --port 8080 api:app --reload
