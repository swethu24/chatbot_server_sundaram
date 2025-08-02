import mysql.connector
from datetime import datetime

def update_order_status():
    cnx = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_food_chat_bot_user",
    password="kwW4Ytz?rqNgFCq",
    database="freedb_food_chat_bot",
    port = 3306            
)
    cursor = cnx.cursor()

    cursor.execute("""
        UPDATE order_tracking
        SET status = "In transit"
        where ststus = "in progress"
    """)

    cursor.execute("""
        UPDATE order_tracking
        SET status = 'delivered'
        WHERE status = 'in transit';
    """)

    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Status updated at {datetime.now()}")


if __name__ == "__main__":
    update_order_status()
    print("Order status update completed.")
