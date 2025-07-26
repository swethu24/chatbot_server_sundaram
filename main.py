from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
async def root(request: Request):
    print(f"Request received: {request.method} {request.url}")
    return {"Hello,World!"}