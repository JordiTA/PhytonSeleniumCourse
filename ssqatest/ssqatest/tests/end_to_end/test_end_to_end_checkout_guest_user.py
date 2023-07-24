import pytest
from ssqatest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def testEndToEndCheckoutGuestUser(self):

        # GO TO HOME PAGE
        home_page = HomePage(self.driver)
        home_page.goToHomePage()

        # ADD 1 ITEM TO CARD

        # GO TO CART

        # APPLY FREE CUPON

        # SLECT FREE SHIPPING

        # CLICK ON CHECKOUT

        # FILL INFORM

        # CLICK ON PLACE ORDER

        # VERIFY ORDER IS RECIEVED

        # VERYFY ORDER IS RECORDED IN DATABASE (via SQL // via API)
        pass