from ssqatest.src.pages.locators import MyAccountSignedOutLocator
from ssqatest.src import SeleniumExtended
from ssqatest.src.helpers.configHelpers import getBaseURL

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def goToMyAccount(self):
        baseURL = getBaseURL()
        accountURL = baseURL + self.endpoint
        self.driver.get(accountURL)

    def inputLoginUsername(self, username):
        self.sl.waitAndInputText(self.LOGIN_USERNAME, username)

    def inputLoginPassword(self, password):
        self.sl.waitAndInputText(self.LOGIN_PASSWORD, password)

    def clickLoginButton(self):
        self.sl.waitAndClick(self.LOGIN_BUTTON)

