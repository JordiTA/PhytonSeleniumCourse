from ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocator
from ssqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verifyUserIsSignedIn(self):
        self.sl.waitUntilElementIsVisible(self.LOGOUT_BUTTON)