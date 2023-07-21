import pytest

pytestmark = [pytest.mark.frontend, pytest.mark.slow]

@pytest.mark.smoke
def testLoginPageValidUser():
    print("")
    print("Login with valid User.")

@pytest.mark.regression
@pytest.mark.smoke
def testLoginWrongPassword():
    print("Login with wrong Password.")

# RUN ONE IN TERMINAL --> pytest -m smoke --> Runs the two functions
# RUN ONE WITH TWO TAGS IN TERMINAL --> pytest -m "smoke and regression" --> Runs only the second function