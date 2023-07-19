from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

url = "file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/iFrames/iFrames_example.html"
driver.get(url)

# ------------------ BUTTON OUT FRAME ------------------ #
driver.find_element(By.ID, 'btnOutFrame').click()

alert = driver.switch_to.alert
alertText = alert.text
assert alertText == 'Just Clicked Outside iFrame', "Should've gotten outside message"
alert.dismiss()

# ------------------ BUTTON IN FRAME ------------------ #
iFrame = driver.find_element(By.ID, 'myFrame1')
driver.switch_to.frame(iFrame)

driver.find_element(By.ID, 'btnInFrame').click()

alert = driver.switch_to.alert
alertText = alert.text
assert alertText == 'Just Clicked Inside iFrame', "Should've gotten outside message"
alert.dismiss()
# Note: You have to switch to driver.switch_to.default_content() to go back to normal