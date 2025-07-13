import pytest
from selenium.webdriver.common.by import By
import random
import time
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddCartPage:
    search_box = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")
    product_links = (By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    brand_filters = (By.CSS_SELECTOR, "li[id^='p_89/']")
    add_to_cart_btn = (By.ID, "add-to-cart-button")
    cart_icon = (By.XPATH, '//*[@id="sw-gtc"]//a | //*[@id="nav-cart-count-container"]')
    Continue_btn = (By.XPATH, "//button[contains(., 'Continue shopping')]")

    def __init__(self, driver, util):
        self.driver = driver
        self.util = util
        self.logger = logging.getLogger(__name__)

    def handle_continue_shopping_popup(self):
        try:
            continue_btn = self.util.wait_until_clickable(self.Continue_btn)
            continue_btn.click()
        except TimeoutException:
            pass

    def search_laptop(self):
        self.util.send_keys(self.search_box, "laptop")
        self.util.click_element(self.search_btn)

    def apply_random_brand_filter(self):
        brands = self.driver.find_elements(*self.brand_filters)
        self.util.execute_script("arguments[0].scrollIntoView();", brands[0])
        if not brands:
            raise Exception("No brand filters visible on Amazon results page")
        chosen = random.choice(brands)
        brand_name = chosen.text.strip()
        self.util.execute_script("arguments[0].click();", chosen)
        time.sleep(3)
        return brand_name

    def select_random_product_and_click(self):
        links = self.util.wait_until_clickable(self.product_links)
        self.util.execute_script("arguments[0].scrollIntoView();", links[0])
        random.choice(links).click()

    def add_to_cart_with_fallback(self):
        try:
            price_option_xpath = "//div[starts-with(@id, 'newAccordionRow')]"
            container = self.util.wait_until_clickable(By.XPATH, price_option_xpath)
            container.click()
            add_btn = self.util.wait_until_clickable(self.add_to_cart_btn)
            add_btn.click()
        except TimeoutException:
            add_btn = self.util.wait_until_clickable(self.add_to_cart_btn)
            add_btn.click()

    def go_to_cart(self):
        view_cart_button = self.util.wait_until_clickable(self.cart_icon)
        view_cart_button.click()

