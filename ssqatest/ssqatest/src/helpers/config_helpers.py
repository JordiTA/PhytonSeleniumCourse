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