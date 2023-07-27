import pytest
import pytest_html
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions

@pytest.fixture(scope="class")
def init_driver(request):
    
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']
    
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The enviroment variable 'BROWSER' must be set.")
    
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")
    
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
    # import pdb; pdb.set_trace()
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extras.append(pytest_html.extras.html('<div style="background:orange">Additional HTML</div>'))
            extras.append(pytest_html.extras.image('file://D:/Udemy/PhytonSeleniumCourse/ssqatest/ssqatest/error_logo.png'))
        report.extra = extras