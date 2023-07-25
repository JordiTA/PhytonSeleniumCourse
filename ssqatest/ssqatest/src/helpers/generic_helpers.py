import random
import string
import logging as logger

def generateRandomEmailAndPassword(domain=None, email_prefix=None):
    
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'
    
    email_lenght = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=email_lenght))

    email = email_prefix + '_' + random_string + '@' + domain

    logger.info(f"Generated random email: ´{email}")

    # PASSWORD BETTER TO BE HARDCODED TO KNOW WHAT IT IS, BUT HERE IT IS THE CODE:
    password_lenght = 16
    password = ''.join(random.choices(string.ascii_letters, k=password_lenght))
    random_info = {
        "email": email,
        "password": password
    }
    return random_info