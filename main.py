from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.post("/")
async def root(request: Request):
    body = await request.json()
    intent = body['queryResult']['intent']['displayName']
    parameters = body['queryResult']['parameters']
    output_contexts = body['queryResult']['outputContexts']
    print(intent)
    return {f"Request received for intent : {intent}"}