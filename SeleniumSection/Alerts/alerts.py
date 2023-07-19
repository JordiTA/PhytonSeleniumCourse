from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

url = "file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/Alerts/alerts_example.html"
driver.get(url)

# # EXAMPLE 1
# You need to deal with alerts if you want to continue testing
alert1Btn = driver.find_element(By.CSS_SELECTOR, '#jsAlertExample > button')
alert1Btn.click()

alert = driver.switch_to.alert
assert alert.text == 'I am a JavaScript Alert', "Unespected text on alert"

alert.accept()
# alert.dismiss()

# # EXAMPLE 2
confirmBtn = driver.find_element('css selector', 'div#jsConfirmExample button')
confirmBtn.click()
alertConfirm = driver.switch_to.alert
# alertConfirm.accept()
# rsMessage = driver.find_element('id', 'userResponse1').text
# assert rsMessage == 'Great! You will love it!', "Wrong message after accepting"

alertConfirm.dismiss()
rsMessage = driver.find_element('id', 'userResponse1').text
assert rsMessage == "Too bad!!! You would've loved it!", "Wrong message after accepting"