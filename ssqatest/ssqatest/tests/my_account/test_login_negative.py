import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def testLogInNoneExistingUser(self):
        print("***********************")
        print("TEST LOGIN NON EXISTING")
        print("***********************")
        account = MyAccountSignedOut(self.driver)

        account.goToMyAccount()
        account.inputLoginUsername('asdfasdf')
        account.inputLoginPassword('asdfadsfa')
        account.clickLoginButton()

        expected_error = 'Error: The password you entered for the username asdfasdf is incorrect. Lost your password?'
        account.waitUntilErrorIsDisplayed(expected_error)