from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from utils import db_connector
from utils import fetch_data

app = FastAPI()
inprogress_orders = {}


@app.post("/")
async def root(request: Request):
    body = await request.json()
    intent = body['queryResult']['intent']['displayName']
    parameters = body['queryResult']['parameters']
    output_contexts = body['queryResult']['outputContexts']
    session_id = fetch_data.extract_session_id(output_contexts[0]["name"])
    print(parameters)
    intent_handler_dict = {
        'order.add': add_to_order,
        'order.remove': remove_from_order,
        'order.complete': complete_order,
        'order.track': track_order
    }

    return intent_handler_dict[intent](parameters, session_id)

def save_to_db(order: dict):
    print("Inside save_to_db")
    next_order_id = db_connector.get_next_order_id()
    print("Got next orer id, adding items")
    # Insert individual items along with quantity in orders table
    for food_item, quantity in order.items():
        rcode = db_connector.insert_order_item(
            food_item,
            quantity,
            next_order_id
        )

        if rcode == -1:
            return -1

    # Now insert order tracking status
    db_connector.insert_order_tracking(next_order_id, "in progress")

    return next_order_id

def complete_order(parameters: dict, session_id: str):
    print("Inside complete_order")
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to a backend error. " \
                               "Please place a new order again"
        else:
            order_total = db_connector.get_total_order_price(order_id)

            fulfillment_text = f"Awesome! Your Order is Placed. " \
                           f"Here is your order id # {order_id}. " \
                           f"Your order total is {order_total} which you can pay at the time of delivery!"

        del inprogress_orders[session_id]

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def add_to_order(parameters: dict, session_id: str):
    print("Inside add to order")
    food_items = parameters["food-item"]
    quantities = parameters["number"]
    print(food_items,quantities)
    if len(food_items) != len(quantities):
        fulfillment_text = " I\'m Sorry, I didn\'t understand. Could you please specify food items and quantities clearly?"
    else:
        new_food_dict = dict(zip(food_items, quantities))

        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict
        else:
            inprogress_orders[session_id] = new_food_dict

        order_str = fetch_data.get_str_from_food_dict(inprogress_orders[session_id])
        fulfillment_text = f"So far you have ordered: {order_str}. Would you like to have anything else?"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def remove_from_order(parameters: dict, session_id: str):
    print("Inside remove from order")
    if session_id not in inprogress_orders:
        return JSONResponse(content={
            "fulfillmentText": "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
        })
    
    food_items = parameters["food-item"]
    current_order = inprogress_orders[session_id]

    removed_items = []
    no_such_items = []
    fulfillment_text = ""

    for item in food_items:
        if item not in current_order:
            no_such_items.append(item)
        else:
            removed_items.append(item)
            del current_order[item]

    if len(removed_items) > 0:
        fulfillment_text = f'Removed {",".join(removed_items)} from your order!'

    if len(no_such_items) > 0:
        fulfillment_text = f' Your current order does not have {",".join(no_such_items)}'

    if len(current_order.keys()) == 0:
        fulfillment_text += " Your order is empty!"
    else:
        order_str = fetch_data.get_str_from_food_dict(current_order)
        fulfillment_text += f" Here is what is left in your order: {order_str}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def track_order(parameters: dict, session_id: str):
    print("Inside track order")
    order_id = int(parameters['order_id'])
    order_status = db_connector.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The current status of order with id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

