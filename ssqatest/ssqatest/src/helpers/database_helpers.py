import pymysql
from ssqatest.src.helpers.config_helpers import getCredentialsDB

def readFromDB(query):

    db_credentials = getCredentialsDB()
    #CONNECT TO DATABASE
    connection = pymysql.connect(host=db_credentials['db_host'], port=db_credentials['db_port'],
                                 user=db_credentials['db_user'], password=db_credentials['db_password'])
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