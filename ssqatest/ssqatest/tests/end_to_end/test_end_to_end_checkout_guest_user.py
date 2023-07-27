import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.OrderRecievedPage import OrderRecievedPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.helpers.database_helpers import getOrderByOrderNumberFromDB

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def testEndToEndCheckoutGuestUser(self):

        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_recieved_page = OrderRecievedPage(self.driver)

        # GO TO HOME PAGE
        home_page.goToHomePage()

        # ADD 1 ITEM TO CARD
        home_page.clickFirstAddToCartButton()

        # MAKE SURE THE CART IS UPDATED
        header.waitUntilCartItemCount(1)

        # GO TO CART
        header.clickOnCartOnRightHeader()

        # VERYFY ITEM IN THE CART
        product_names = cart_page.getAllProductNamesInCart()
        assert len(product_names) == 1, f"Expected 1 product in cart but found {product_names} products."

        # APPLY FREE CUPON
        cupon_code = GenericConfigs.FREE_CUPON
        cart_page.applyCuppon(cupon_code)

        # SELECT FREE SHIPPING --> NO NEED TO DO THAT WHEN WE WORK IN localhost:8888, only in demostore.
        # cart_page.clickShippingOption()

        # CLICK ON CHECKOUT
        cart_page.clickOnProceedToCheckout()

        # FILL INFORM
        checkout_page.fillInBillingInfo()

        # CLICK ON PLACE ORDER
        checkout_page.clickPlaceHolder()

        # VERIFY ORDER IS RECIEVED
        order_recieved_page.verifyOrderRecievedPageLoaded()

        # WAIT BECAUSE IT DOES NOT WAIT FOR THE QUERY TO BE SEND BY THE WEBSITE, THIS CAUSES AN ERROR
        header.waitUntilCartItemCount(0)

        # VERYFY ORDER IS RECORDED IN DATABASE (via SQL // via API)
        order_number = order_recieved_page.getOrderNumber()
        print('************')
        print(order_number)
        print('************')

        db_order = getOrderByOrderNumberFromDB(order_number)
        assert db_order, f"After creating order with FE, not found in DB. Order number: {order_number}."