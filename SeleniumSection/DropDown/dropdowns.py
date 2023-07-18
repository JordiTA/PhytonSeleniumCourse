from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # Import de Select
from selenium.webdriver.chrome.options import Options

import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

url = 'file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/DropDown/drop_down_example.html'

driver.get(url)

# # OPTION 1: Using Select Class
dropdown = driver.find_element(By.ID, 'age-range-select')

dropdownObj = Select(dropdown)

dropdownObj.select_by_index(1)
dropdownObj.select_by_value('21-40')

allOptions = dropdownObj.options
for option in allOptions:
    print(option.text)

# # OPTION 2: Button
selectBtn = driver.find_element(By.ID,'dropdownMenuButton')
selectBtn.click()
time.sleep(5)
myOption = driver.find_element(By.CSS_SELECTOR, '#dropdowns > div:nth-child(3) > div > ul > li:nth-child(1) > a')
myOption.click()