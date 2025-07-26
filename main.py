from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def handler(request:Request):
    """Handles incoming requests to the root endpoint."""
    input_payload = await request.json()
    print(f"Received request: {input_payload}")
    intent = input_payload['queryResult']['intent']['displayName']
    parameters = input_payload['queryResult']['parameters']
    output_context = input_payload['queryResult']['outputContexts']

    if intent == "order.track":
        return {f"Received request at backend {intent}"}