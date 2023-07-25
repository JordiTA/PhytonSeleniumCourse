from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def waitAndInputText(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def waitAndClick(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def waitUntilElementContainsText(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    
    def waitUntilElementIsVisible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def waitAndGetElements(self, locator, timeout=None, error=None):
        timeout = timeout if timeout else self.default_timeout

        error = error if error else f"Unable to find elements located by '{locator}'," \
                                    f"after timeout of {timeout}."

        try:
            elements = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(error)
        
        return elements
    
    def waitAndGetText(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element_text = element.text
        return element_text

