from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()

driver.get('http:/demostore.supersqa.com')

cartElement = driver.find_element(By.LINK_TEXT, 'Cart')
print(cartElement.text)

accountElement = driver.find_element(By.LINK_TEXT, 'My account')
print(accountElement.text)

accountElementPartial = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(accountElementPartial.text)

footerLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(footerLink.text)

# Must be <a> tag or it will fail
# driver.find_element(By.LINK_TEXT, '0 items') # ----> ERROR