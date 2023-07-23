from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.defaultTimeout = 10

    def waitAndInputText(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.defaultTimeout
        
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def waitAndClick(self, locator, timeout=None):
        timeout = timeout if timeout else self.defaultTimeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()