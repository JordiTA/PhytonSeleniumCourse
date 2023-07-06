from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pdb
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)
driver.get('http:/demostore.supersqa.com')

cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
time.sleep(3)
cart.click()

myAccount = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
myAccount.click()

time.sleep(3)
driver.quit()