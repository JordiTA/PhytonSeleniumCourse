from ssqatest.src.helpers.configHelpers import getBaseURL

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def goToHomePage(self):
        home_url = getBaseURL()
        self.driver.get(home_url)