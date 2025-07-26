from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.post("/")
async def root(request: Request):
    body = await request.json()
    print("Received Dialogflow Webhook Request:")
    print(json.dumps(body, indent=2))

    #print("Request JSON: ", json.dumps(request_info, indent=2))

    return {"Request received at backend"}