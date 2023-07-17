from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pdb

driverOptions = Options()
driverOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driverOptions)

driver.get('http://demostore.supersqa.com')

searchField = driver.find_element(By.ID, 'woocommerce-product-search-field-0')

# # EXAMPLE 1: Place Holder
placeHolder = searchField.get_attribute('placeholder')
if placeHolder != "Search products…":
    raise Exception("Place Holder for search field is not as expected. ACTUAL: {}".format(placeHolder))
else:
    print("PASS")

# # EXAMPLE 2: See which tab is selected
account = driver.find_element(By.CSS_SELECTOR, 'li.page-item-9')
account.click()

navItems = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li')

for item in navItems:
    itemClass = item.get_attribute('class')
    if 'current_page_item' in itemClass:
        print(f"The selected tab is: {item.text}.")

driver.back()

# # EXAMPLE 3: Get link URL
productLink = driver.find_element(By.CSS_SELECTOR, 'li.product a')
productURL = productLink.get_attribute('href')
print(f"The URL for product is : {productURL}")