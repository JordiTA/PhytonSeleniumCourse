import os

def getBaseURL():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        # return 'http://demostore.supersqa.com'
        return 'http://localhost:8888/quicksite/'
    elif env.lower() == 'prod':
        return 'http://demostore.prod.supersqa.com'
    else:
        raise Exception(f"Unknown enviroment: {env}")
    
def getCredentialsDB():
    env = os.environ.get('ENV', 'test')

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    if not db_user or not db_password:
        raise Exception("Enviroment variables 'DB_USER' & 'DB_PASSWORD' must be set.")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown enviroment: {env}")
    
    db_info = {"db_host": db_host, "db_port": db_port,"db_user": db_user, "db_password": db_password}
    
    return db_info