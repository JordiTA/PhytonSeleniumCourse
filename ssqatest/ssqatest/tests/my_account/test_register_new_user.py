import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.helpers.generic_helpers import generateRandomEmailAndPassword

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def testRegisterValidNewUser(self):
        account = MyAccountSignedOut(self.driver)
        account.goToMyAccount()

        random_email = generateRandomEmailAndPassword()
        account.inputRegisterEmail(random_email)
        account.inputRegisterPassword('Abcdefg12345!')
        account.clickRegisterButton()

        #verify user is registered