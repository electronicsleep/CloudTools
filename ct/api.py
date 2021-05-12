from typing import Optional
from fastapi import FastAPI
from ct_inv import server_list

app = FastAPI()


@app.get("/")
def read_root():
    return {"Cloud": "Tools"}


@app.get("/health")
def read_health():
    return {"Status": "Up"}


@app.get("/inv")
def read_inv():
    payload = {'sites': server_list}
    return payload


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
