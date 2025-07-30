import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_food_chat_bot_user",
    password="kwW4Ytz?rqNgFCq",
    database="freedb_food_chat_bot",
    port = 3306            
)

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