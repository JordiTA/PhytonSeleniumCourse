from selenium.webdriver.common.by import By

class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    CUPON_FIELD = (By.ID, 'coupon_code')
    APPLY_CUPON_BUTTON = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    CART_PAGE_MESSAGE = (By.CLASS_NAME, 'woocommerce-message')
    SHIPPING_OPTION = (By.CSS_SELECTOR, 'input[id="shipping_method_0_local_pickup3"]')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR,  'a.checkout-button')