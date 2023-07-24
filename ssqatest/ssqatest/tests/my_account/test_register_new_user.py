import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.generic_helpers import generateRandomEmailAndPassword

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def testRegisterValidNewUser(self):
        account_out = MyAccountSignedOut(self.driver)
        account_in = MyAccountSignedIn(self.driver)

        account_out.goToMyAccount()

        random_email = generateRandomEmailAndPassword()
        account_out.inputRegisterEmail(random_email)
        account_out.inputRegisterPassword('Abcdefg12345!')
        account_out.clickRegisterButton()

        #verify user is registered
        account_in.verifyUserIsSignedIn()