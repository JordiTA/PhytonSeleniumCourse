from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)


#------------------------ SEND KEYS --> TEXT ------------------------------------
driver.get('http://demostore.supersqa.com/my-account/')

username = driver.find_element(By.ID, 'username')
username.send_keys('User1')

password = driver.find_element(By.ID, 'password')
password.send_keys('1234')

submitBtn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
submitBtn.click()

#------------------------ SEND KEYS --> IMPORT KEYS ------------------------------------
driver.get('http://demostore.supersqa.com')

from selenium.webdriver.common.keys import Keys

searchField = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
searchField.send_keys('hoodie')
time.sleep(3)
searchField.send_keys(Keys.ENTER)

#------------------------ SEND KEYS --> IMPORT KEYS 2 ------------------------------------
driver.get('http://demostore.supersqa.com/my-account/')

username = driver.find_element(By.ID, 'username')
username.send_keys('User1')
time.sleep(3)
username.send_keys(Keys.TAB)