#!/bin/bash
cd ct
uvicorn --port 8080 api:app --reload
