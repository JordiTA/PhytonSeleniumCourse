import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os

@pytest.fixture(scope="class")
def init_driver(request):
    
    supportedBrowsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']
    
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The enviroment variable 'BROWSER' must be set.")
    
    browser = browser.lower()
    if browser not in supportedBrowsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supportedBrowsers}")
    
    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        ff_options = FFOptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--no-sandbox')
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(options=ff_options)

    request.cls.driver = driver
    yield
    driver.quit()