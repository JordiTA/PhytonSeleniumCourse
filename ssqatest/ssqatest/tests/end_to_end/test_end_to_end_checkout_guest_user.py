import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def testEndToEndCheckoutGuestUser(self):

        home_page = HomePage(self.driver)
        header = Header(self.driver)
        
        # GO TO HOME PAGE
        home_page.goToHomePage()

        # ADD 1 ITEM TO CARD
        home_page.clickFirstAddToCartButton()

        # GO TO CART
        header.clickOnCart()

        # APPLY FREE CUPON

        # SLECT FREE SHIPPING

        # CLICK ON CHECKOUT

        # FILL INFORM

        # CLICK ON PLACE ORDER

        # VERIFY ORDER IS RECIEVED

        # VERYFY ORDER IS RECORDED IN DATABASE (via SQL // via API)
        pass