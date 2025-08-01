import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_food_chat_bot_user",
    password="kwW4Ytz?rqNgFCq",
    database="freedb_food_chat_bot",
    port = 3306            
)
def insert_order_item(food_item, quantity, order_id):
    cursor = cnx.cursor()
    items = dict(zip(food_item, quantity))

    for item_name, qty in items.items():
        # Fetch item_id and price from food_items table
        cursor.execute("SELECT item_id, price FROM food_items WHERE name = %s", (item_name,))
        result = cursor.fetchone()

        if result:
            item_id, price = result
            total_price = price * qty

            # Insert into orders table
            insert_query = """
                INSERT INTO orders (order_id, item_id, quantity, total_price)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (order_id, item_id, qty, total_price))
        else:
            print(f"Item '{item_name}' not found in food_items table.")

    cnx.commit()
    cursor.close()

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))
    cnx.commit()
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()
    query = f"SELECT o.order_id, SUM(fi.price * o.quantity) AS total_price FROM orders o JOIN food_items fi ON o.item_id = fi.item_id where o.order_id = {order_id} GROUP BY o.order_id;"
    cursor.execute(query)
    result = cursor.fetchone()[1]
    cursor.close()
    return result

def get_next_order_id():
    cursor = cnx.cursor()
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    result = cursor.fetchone()[0]
    cursor.close()

    if result is None:
        return 1
    else:
        return result + 1

def get_order_status(order_id):
    cursor = cnx.cursor()
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]
    else:
        return None