from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import string
import random

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(10)

url = 'http://demostore.supersqa.com/my-account/'
driver.get(url)

# SETTING VARIABLES
emailFieldID = 'reg_email'
passwordFieldID = 'reg_password'
logoutBtnCSS = 'li.woocommerce-MyAccount-navigation-link--customer-logout a'

# FIND EMAIL FIELD
emailField = driver.find_element(By.ID, emailFieldID)

# GENERATE RANDOM EMAIL
letters = string.ascii_lowercase
randomString = ''.join(random.choice(letters)for i in range(15))
randomEmail = randomString + "@gmail.com"

# TYPE IN THE EMAIL FIELD
emailField.send_keys(randomEmail)

# FIND PASSWORD FIELD AND ENTER PASSWORD
passwordField = driver.find_element(By.ID, passwordFieldID)
passwordField.send_keys('MyPassword123!')

# CLICK REGISTER BUTTON
registerBtn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
time.sleep(3)
registerBtn.click()

try:
    logoutBtn = driver.find_element(By.CSS_SELECTOR, logoutBtnCSS)
except:
    raise Exception("!!!User not logged in aafter register!!!")