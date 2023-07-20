from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

url = "file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/MultipleWindowsAndTabs/windows-and_tabs_example.html"
driver.get(url)

driver.find_element(by.XPATH, '//*[@id="windows"]/a[1]').click()

# heading = driver.find_element(by.XPATH, '/html/body/h1').text

print("Before switching focus:" + driver.title)

allWindows = driver.window_handles
originalWindow = allWindows[0]
newWindow = allWindows[1]

driver.switch_to.window(newWindow)
print("After switching focus:" + driver.title)

print("Closing tab...")
driver.close()

print("Switching back to original...")
driver.switch_to.window(originalWindow)