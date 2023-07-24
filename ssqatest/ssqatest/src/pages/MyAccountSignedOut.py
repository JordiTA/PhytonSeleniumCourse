from ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.configHelpers import getBaseURL
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def goToMyAccount(self):
        baseURL = getBaseURL()
        accountURL = baseURL + self.endpoint

        logger.info(f"Going to {accountURL}")
        self.driver.get(accountURL)

    def inputLoginUsername(self, username):
        self.sl.waitAndInputText(self.LOGIN_USERNAME, username)

    def inputLoginPassword(self, password):
        self.sl.waitAndInputText(self.LOGIN_PASSWORD, password)

    def clickLoginButton(self):
        logger.info("Clicking 'LOGIN' button.")
        self.sl.waitAndClick(self.LOGIN_BUTTON)

    def waitUntilErrorIsDisplayed(self, exp_err):
        self.sl.waitUntilElementContainsText(self.ERRORS_UL, exp_err)

