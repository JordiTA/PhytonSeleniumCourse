from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10) # # IMPLICIT WAIT !!!

driver.get('file:///D:/Udemy/Correccion/SELENIUM_SECTION/Waits/page_with_slow_image.html')

image = driver.find_element(By.ID, 'the_slow_image')
image.click()
print("Found image!!!")