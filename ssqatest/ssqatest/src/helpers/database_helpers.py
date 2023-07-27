import pymysql

def readFromDB(query):

    #CONNECT TO DATABASE
    connection = pymysql.connect(host='127.0.0.1', port=8889,
                                 user='root', password='root')
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # RETURN THE RESULT
    return db_data

def getOrderByOrderNumberFromDB(order_number):

    query = f"SELECT * FROM quicksitedb.wp_posts WHERE ID = {order_number} AND post_type = 'shop_order';"

    db_order = readFromDB(query)
    return db_order