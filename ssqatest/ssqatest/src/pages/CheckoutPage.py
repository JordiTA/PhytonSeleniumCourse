from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.generic_helpers import generateRandomEmailAndPassword

class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def inputBillingFirstName(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFName'
        self.sl.waitAndInputText(self.BILLING_FIRST_NAME_FIELD, first_name)

    def inputBillingLastName(self, last_name=None):
        last_name = last_name if last_name else 'AutomationLName'
        self.sl.waitAndInputText(self.BILLING_LAST_NAME_FIELD, last_name)

    def inputBillingStreetAddress(self, address1=None):
        address1 = address1 if address1 else '123 Main st.'
        self.sl.waitAndInputText(self.BILLING_ADDRESS_FIELD, address1)

    def inputBillingCity(self, city=None):
        city = city if city else 'San Francisco'
        self.sl.waitAndInputText(self.BILLING_CITY_FIELD, city)
    
    def inputBillingZip(self, zip=None):
        zip = zip if zip else 94016
        self.sl.waitAndInputText(self.BILLING_ZIP_FIELD, zip) 
    
    def inputBillingPhoneNumber(self, phone=None):
        phone = phone if phone else '4151111111'
        self.sl.waitAndInputText(self.BILLING_PHONE_FIELD, phone) 
    
    def inputBillingEmail(self, email=None):
        if not email:
            random_email = generateRandomEmailAndPassword()
            email = random_email['email']
        
        self.sl.waitAndInputText(self.BILLING_EMAIL_FIELD, email) 

    def fillInBillingInfo(self, first_name=None, last_name=None, address1=None, city=None, zip=None, phone=None, email=None):
        self.inputBillingFirstName(first_name)
        self.inputBillingLastName(last_name)
        self.inputBillingStreetAddress(address1)
        self.inputBillingCity(city)
        self.inputBillingZip(zip)
        self.inputBillingPhoneNumber(phone)
        self.inputBillingEmail(email)

    def clickPlaceHolder(self):
        self.sl.waitAndClick(self.PLACE_HOLDER_BUTTON)