"""
Question: Write a function that will keep retrying to check a status of a process by calling
the function "is_status_success()" until the the function returns True.

Retry for 20 seconds  while sleeping 3 seconds between each retry. After the 20 seconds raise an exception
if the success check is not True.
Make the max retry length and the sleep time keyword parameters to the function with default values.

The function to call to check the status is writen below. The function will randomly return True or False.
Call the function in the loop as a way of checking success status of a process.

Requirement:
    - Use while loop
    - Use timer
    - Raise an Exception
    - keyword parameter for max retry
    - keyword parameter for sleep time between retries

Hint:
    To set a timer you can import time and to set a timeout you can do
        > time.time() + 20 # this will set a timeout 20 min from now. time.time() is now.
"""

import random
import time

def is_status_success():
    """
    Check the status of a process and return True if status is success and False if not.
    :return:
    """
    print("Checking the status of the process.")
    list_to_chose_from = [True, True, False, False, False, False, False]

    bool_to_return = random.choice(list_to_chose_from)

    return bool_to_return


def wait_and_retry_until_status_is_success(maxWait = 20, sleep = 3):
    
    timeout = time.time() + maxWait
    while time.time() <= timeout:
        returnedBool = is_status_success()
        if returnedBool:
            print("Status Success is TRUE!!!")
            break
        else:
            print("Status Success is FALSE.")
            time.sleep(sleep)
    else:
        print("Has not succed because of timeout!")

wait_and_retry_until_status_is_success()