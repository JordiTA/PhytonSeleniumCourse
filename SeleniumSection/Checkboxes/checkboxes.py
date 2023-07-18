from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

url = "file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/Checkboxes/checkbox_example.html"

driver.get(url)

time.sleep(3)

# # # EXAMPLE 1 # # #
selectValue = "61-80"
locatorValue = f'input[name="age-group-checkbox"][value="{selectValue}"]'

choice = driver.find_element(By.CSS_SELECTOR, locatorValue)
choice.click()

assert choice.is_selected(), f"After clicking value {selectValue} it is not selected"

# # # EXAMPLE 2 # # # VERIFY ALL THE CHECKBOXES

expectedCheckboxes = 4
allCheckboxes = driver.find_elements(By.NAME, 'age-group-checkbox')

assert len(allCheckboxes == expectedCheckboxes), "Number of checkboxes is not expected"

for checkbox in allCheckboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with the value {value} is selectable")
    else:
        raise Exception(f"Checkbox with the value {value} is not selectable")