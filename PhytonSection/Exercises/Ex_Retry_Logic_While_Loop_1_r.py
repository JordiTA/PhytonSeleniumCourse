"""
Question:
    Write a function that will keep retrying to check a status of a process by calling
    the function is_status_success() until the the function returns True.

    Retry 10 times and sleep 3 seconds each retry. After the 10th try raise an exception.
    Make the retry count and the sleep time keyword parameter to the function with default values.

    The function to call to check the status is writen below. The function will randomly return True or False.
    Call the function in the loop as a way of checking success status of a process.

Requirement:
    - Use while loop
    - Use counter
    - Raise an Exception
    - keyword parameter for max retry
    - keyword parameter for sleep time between retries
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


def retry_with_counter_until_status_is_success():
    
    counter = 0

    while counter < 10:
        counter = counter + 1
        print(f"Try number {counter}")
        returnedBool = is_status_success()
        
        if returnedBool:
            print("Status Success is TRUE!!!")
            break
        else:
            print("Status Success is FALSE.")
            time.sleep(3)
    
    if counter >= 10:
        raise Exception(f"The process did not succed after trying {counter} times.")

retry_with_counter_until_status_is_success()