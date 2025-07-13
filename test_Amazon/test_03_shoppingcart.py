import pytest
from PageObjects.ShoppingCart_Page import ShoppingCartPage
from Utilities. Reusable_Method import ReusableMethod

@pytest.mark.usefixtures("setup")
class TestShoppingCart:
    def test_shopping_cart(self):
        util = ReusableMethod(self.driver)
        cart_page = ShoppingCartPage(self.driver, util)

        cart_page.go_to_cart()
        assert cart_page.get_cart_items() >= 2, "less than 2 items"

        initial_total = cart_page.get_subtotal()
        cart_page.change_quantity(1)
        util.wait_until_clickable(cart_page.subtotal)
        assert cart_page.get_subtotal() <= initial_total, "subtotal didn't reduce"

        cart_page.save_item_for_later()
        assert cart_page.get_cart_items() >= 1, "No item left"
        cart_page.move_to_cart_links()
        assert cart_page.get_cart_items() >= 2, "Item didn't move"



