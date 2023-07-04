# ALL ABOUT DRIVERS: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# # Selenium 3 Example
# driver = webdriver.Chrome(executable_path = "D:\\Udemy\\chromedriver_win32\\chromedriver.exe")

# driver.get("https://google.com")

# # Selenium 4 Example
se = Service(executable_path = "D:\\Udemy\\chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(service=se)

driver.get("https://google.com")

breakpoint()