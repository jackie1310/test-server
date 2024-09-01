from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

@app.get("/")
def test():
    return {"Hello": "This is a test server"}