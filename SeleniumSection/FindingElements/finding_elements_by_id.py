from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pdb

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http:/demostore.supersqa.com')

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()

driver.get('http:/demostore.supersqa.com/my-account/')
pdb.set_trace()

# NOTE: to find available methods just do dir(<variable>)
# Example: dir(driver)
# Example: dir(cart)
