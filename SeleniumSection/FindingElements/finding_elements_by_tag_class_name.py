from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get('http:/demostore.supersqa.com')

###    Finding By CLASS NAME    ###
product = driver.find_element(By.CLASS_NAME, "product") # Just find the first one
print(product)
products = driver.find_elements(By.CLASS_NAME, "product") # Returns a list of elements
print(products)

###    Finding By NAME    ###
orderBy = driver.find_element(By.NAME,"orderby")
print(orderBy.text)

###    Finding By NAME    ###
all_a = driver.find_elements(By.TAG_NAME, "a")
print(f"Found number of 'a' tags: {len(all_a)}.")
all_li = driver.find_elements(By.TAG_NAME, "li")
print(f"Found number of 'li' tags: {len(all_li)}.")

pdb.set_trace()