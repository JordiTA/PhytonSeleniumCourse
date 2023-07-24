from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def clickOnCart(self):
        self.sl.waitAndClick(self.CART_RIGHT_HEADER)