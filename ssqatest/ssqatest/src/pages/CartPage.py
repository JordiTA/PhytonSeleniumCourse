from ssqatest.src.SeleniumExtended import SeleniumExtended

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)