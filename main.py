from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def hanlder(request:Request):
    """Handles incoming requests to the root endpoint."""
    #Fetch payload
    input_payload = await request.json()

    intent = input_payload['queryResult']['intent']['displayName']
    parameters = input_payload['queryResult']['parameters']
    output_context = input_payload['queryResult']['outputContexts']

    if intent == "order.track":
        return JSONResponse(
            content={
                "fulfillmentText": "Received request for tracking - Intent : {intent}",
            }
        )