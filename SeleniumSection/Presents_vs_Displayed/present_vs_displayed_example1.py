from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/Presents_vs_Displayed/present_vs_displayed.html'

driver.get(url)

btn1 = driver.find_element(By.ID, 'btn1')
btn1_txt = btn1.text
print(f"First button text: {btn1_txt}")
btn2 = driver.find_element(By.ID, 'btn2')
btn2_txt = btn2.text
print(f"First button text: {btn2_txt}")
btn3 = driver.find_element(By.ID, 'btn3')
btn3_txt = btn3.text
print(f"First button text: {btn3_txt}")
btn4 = driver.find_element(By.ID, 'btn4')
btn4_txt = btn4.text
print(f"First button text: {btn4_txt}")

if btn4.is_displayed():
    btn4.click()
else:
    raise Exception("Button 4 is not displayed")

pdb.set_trace()