import time
import pytest
from PageObjects.AddCart_Page import AddCartPage
from Utilities.Reusable_Method import ReusableMethod

@pytest.mark.usefixtures("setup")
class TestRandomAddCart:

    def test_add_random_laptop_to_cart(self):
        util = ReusableMethod(self.driver)
        page = AddCartPage(self.driver, util)

        self.driver.get("https://www.amazon.in")
        page.handle_continue_shopping_popup()
        page.search_laptop()
        time.sleep(10)
        if "robot" in self.driver.page_source:
            pytest.fail("CAPTCHA detected. Cannot proceed.")
            time.sleep(10)
        page.apply_random_brand_filter()
        time.sleep(8)

        page.select_random_product_and_click()
        time.sleep(7)
        page.add_to_cart_with_fallback()
        page.go_to_cart()

        assert "Shopping Cart" in self.driver.title or "Sub-Total" in self.driver.page_source
