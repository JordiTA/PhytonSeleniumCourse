from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators

class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def getAllProductNamesInCart(self):
        product_name_elements = self.sl.waitAndGetElements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names
    
    def inputCupon(self, cupon_code):
        self.sl.waitAndInputText(self.CUPON_FIELD, cupon_code)

    def clickApplyCupon(self):
        self.sl.waitAndClick(self.APPLY_CUPON_BUTTON)

    def applyCuppon(self, cupon_code):
        self.inputCupon(cupon_code)
        self.clickApplyCupon()
        success_msg = self.getDisplayedMessage()
        assert success_msg == 'Coupon code applied successfully.', f"Unexpected message when applying cupon."

    def getDisplayedMessage(self):
        text = self.sl.waitAndGetText(self.CART_PAGE_MESSAGE)
        return text
    
    def clickShippingOption(self):
        self.sl.waitAndClick(self.SHIPPING_OPTION)

    def clickOnProceedToCheckout(self):
        self.sl.waitAndClick(self.PROCEED_TO_CHECKOUT_BTN)