from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def clickOnCart(self):
        self.sl.waitAndClick(self.CART_RIGHT_HEADER)

    def waitUntilCartItemCount(self, count):
        if count == 1:
            expected_text = str(count) +' item'
        elif count > 1:
            expected_text = str(count) +' items'
        
        self.sl.waitUntilElementContainsText(self.CART_ITEM_COUNT, expected_text)
