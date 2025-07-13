from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ShoppingCartPage:
    Shopping_cart_button = (By.ID, "nav-cart")
    item_titles = (By.CSS_SELECTOR, ".sc-product-title")
    quantity_dropdowns = (By.NAME, "quantity")
    save_for_later_links = (By.LINK_TEXT, "Save for later")
    move_to_cart_links = (By.LINK_TEXT, "Move to Cart")
    subtotal = (By.ID, "sc-subtotal-amount-activecart")

    def _init_(self, driver, util):
        self.driver = driver
        self.util = util

    def go_to_cart(self):
        self.util.click_element(self.Shopping_cart_button)

    def get_cart_items(self):
       return [item.text for item in self.driver.find_element(*self.item_titles)]

    def change_quantity(self, qty: int):
        dropdowns = self.driver.find_element(*self.quantity_dropdowns)
        if not dropdowns:
            raise Exception
        Select(dropdowns[0]).select_by_value(str(qty))
        self.util.capture_screenshot("quantity_changed")

    def save_item_for_later(self):
        links = self.driver.find_element(*self.save_for_later_links)
        if links:
             self.util.execute_script("argument[0].click;", links[0])
             self.util.capture_screenshot("save_for_later")

    def move_item_to_cart(self):
        links = self.driver.find_element(*self.move_to_cart_links)
        if links :
            self.util.execute_script("argument[0].click;", links[0])
            self.util.capture_screenshot("moved_to_cart")

    def get_subtotal(self):
        return self.util.get_text(self.subtotal)








