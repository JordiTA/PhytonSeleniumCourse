import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def testRegisterValidNewUser(self):
        account = MyAccountSignedOut(self.driver)
        account.goToMyAccount()

        account.inputRegisterEmail('admastest1@supersqa.com')
        account.inputRegisterPassword('Abcdefg12345!')
        account.clickRegisterButton()

        #verify user is registered