from selenium import webdriver
import pdb

# # CHROME


driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')
pdb.set_trace()


# # FIREFOX // Need to download driver for this code to work --> {geckodriver}

'''
driver = webdriver.Firefox()
driver.get('http://demostore.supersqa.com')
pdb.set_trace()
'''

# # SAFARI // Need to download driver for this code to work

'''
driver = webdriver.Safari()
driver.get('http://demostore.supersqa.com')
pdb.set_trace()
'''