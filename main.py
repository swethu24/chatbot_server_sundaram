from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from utils import db_connector

app = FastAPI()

@app.post("/")
async def root(request: Request):
    body = await request.json()
    intent = body['queryResult']['intent']['displayName']
    parameters = body['queryResult']['parameters']
    output_contexts = body['queryResult']['outputContexts']
    
    if intent == "order.track":
        return fetch_tracking_status(parameters["order_id"])
    
def fetch_tracking_status(order_id):
    """Fetch Tracking Status"""
    order_status = db_connector.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


