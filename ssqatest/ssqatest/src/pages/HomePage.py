from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import getBaseURL
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def goToHomePage(self):
        home_url = getBaseURL()
        self.driver.get(home_url)

    def clickFirstAddToCartButton(self):
        self.sl.waitAndClick(self.ADD_TO_CART_BUTTON)