from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

url = 'file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/Radios/radios_example.html'
driver.get(url)

expectedValue = '21-40'

locatorValue = 'input[name="age-group-radio"][value="{value}"]'

# # EXAMPLE 1: Verify default is selected
defaultElement = driver.find_element(By.CSS_SELECTOR, locatorValue.format(value=expectedValue))
assert defaultElement.is_selected(), f"The default value of {expectedValue} is not selected."

# # EXAMPLE 2
expectedValues = ['21-40','41-60','61-80','81+','foo']
allRadios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(allRadios) == len(expectedValues), "The number of radios does not match the expected." \
                                              "Expected: {}, Actual: {}".format(len(expectedValues), len(allRadios))