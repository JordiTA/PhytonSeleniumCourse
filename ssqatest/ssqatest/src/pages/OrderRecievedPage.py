from ssqatest.src.pages.locators.OrderRecievedPageLocators import OrderRecievedPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended

class OrderRecievedPage(OrderRecievedPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verifyOrderRecievedPageLoaded(self, expected_text=None):
        expected_text = expected_text if expected_text else 'Order received'
        self.sl.waitUntilElementContainsText(self.PAGE_MAIN_HEADER, expected_text)