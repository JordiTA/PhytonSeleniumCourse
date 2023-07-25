import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def testEndToEndCheckoutGuestUser(self):

        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)

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

        # SLECT FREE SHIPPING

        # CLICK ON CHECKOUT

        # FILL INFORM

        # CLICK ON PLACE ORDER

        # VERIFY ORDER IS RECIEVED

        # VERYFY ORDER IS RECORDED IN DATABASE (via SQL // via API)
        pass