from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pdb

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)
wait = WebDriverWait(driver, 5)

url = "file:///D:/Udemy/PhytonSeleniumCourse/SeleniumSection/Presents_vs_Displayed/present_vs_visible_example_with_cars.html"

driver.get(url)

# series6 = driver.find_element(By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')
# series6.click()

# series6 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))

bmw_btn = driver.find_element(By.CSS_SELECTOR, '#bmw')
bmw_btn.click()

series6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))