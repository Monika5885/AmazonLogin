from selenium import webdriver
import time
import pytest
from PageObjects.Checkout_Page import Checkout_Page
from Utilities.Reusable_Method import ReusableMethod

@pytest.mark.usefixtures("setup")
class TestCheckout:
    def test_checkout(self):
        util = ReusableMethod(self.driver)
        cart_page = Checkout_Page(self.driver, util)
        cart_page.click_account_menu()
        print("Cart open")
        cart_page.click_Checkout()
        print("proceed to checkout")
        time.sleep(5)








