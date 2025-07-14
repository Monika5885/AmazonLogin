import time
import pytest
from PageObjects.AddCart_Page import AddCartPage
from Utilities.Reusable_Method import ReusableMethod

@pytest.mark.usefixtures("setup")
class TestRandomAddCart:

    def test_add_random_laptop_to_cart(self):
        util = ReusableMethod(self.driver)
        page = AddCartPage(self.driver, util)
        login = LoginPage(self.driver, util)
        login.login(util.getusername(config), util.getpassword(config))

        page.handle_continue_shopping_popup()
        page.search_laptop("laptop")
        time.sleep(10)
        if page.is_captcha_present():
            util.capture_screenshots("captcha_detected")
            pytest.skip("CAPTCHA shown")
        page.apply_random_brand_filter()
        time.sleep(8)

        page.select_random_product_and_click()
        time.sleep(7)
        page.add_to_cart_with_fallback()
        page.go_to_cart()

        assert "Shopping Cart" in self.driver.title or "Sub-Total" in self.driver.page_source
