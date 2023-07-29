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

        expected_error = 'Error: The username asdfasdf is not registered on this site. If you are unsure of your username, try your email address instead.'
        account.waitUntilErrorIsDisplayed(expected_error)