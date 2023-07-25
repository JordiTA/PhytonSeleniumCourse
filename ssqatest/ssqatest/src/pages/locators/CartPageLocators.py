from selenium.webdriver.common.by import By

class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    CUPON_FIELD = (By.ID, 'coupon_code')
    APPLY_CUPON_BUTTON = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')

    CART_PAGE_MESSAGE = (By.CLASS_NAME, 'woocommerce-message')