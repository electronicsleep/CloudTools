#!/usr/bin/env python3

from typing import Optional
from fastapi import FastAPI
from ct_inv import server_list

app = FastAPI()


@app.get("/")
def read_root():
    return {"CloudTools": "http://127.0.0.1:8080/api"}


@app.get("/health")
def read_health():
    return {"Status": "Up"}


@app.get("/api")
def read_inv():
    payload = {'sites': server_list}
    return payload


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
