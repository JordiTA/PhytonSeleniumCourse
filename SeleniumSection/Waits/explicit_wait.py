from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('file:///D:/Udemy/Correccion/SELENIUM_SECTION/Waits/page_with_slow_image.html')

# image = driver.find_element(By.ID, 'the_slow_image')
wait = WebDriverWait(driver, 10)

image = wait.until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))

print("Found image!!!")