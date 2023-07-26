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