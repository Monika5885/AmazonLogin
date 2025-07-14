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
    brand_filters = (By.ID, "brandsRefinements")
    add_to_cart_btn = (By.ID, "add-to-cart-button")
    hidden_price_row = (By.XPATH, "//div[starts-with(@id,'newAccordionRow')]")
    cart_icon_any = (By.XPATH, "//*[@id="sw-gtc"]//a | //*[@id="nav-cart-count-container"]")

    def __init__(self, driver, util):
        self.driver = driver
        self.util = util
        self.logger = logging.getLogger(__name__)

    def handle_continue_shopping_popup(self):
        try:
            continue_btn = self.util.wait_until_clickable(self.Continue_btn)
            continue_btn.click()
        except TimeoutException:
            self.logger.debug("No contine shopping")

    def search_laptop(self):
        self.util.send_keys(self.search_box, "laptop")
        self.util.click_element(self.search_btn)

    def is_captcha_present(self) -> bool:
    page = self.driver.page_source.lower()
    return "Sorry, we just need to make sure you're not a robot" in page or "captcha" in page

    def apply_random_brand_filter(self):
    try:
        brands = self.driver.find_elements(*self.brand_filters)
        brand_lables = brands.find_elements(By.XPATH, ".//li//span[@class='a-size-base a-color-base']")
        self.util.execute_script("arguments[0].scrollIntoView();", brands[0])
        if not brand_lables:
            raise Exception("No brand filters visible on Amazon results page")
            
        chosen_label = random.choice(brand_lables)
        brand_name = chosen_label.text.strip()
        checkbox = chosen_label.find_element(By.XPATH, "./preceding-sibling::div//input")
        self.driver.execute_script("arguments[0].click();", chosen)
        time.sleep(3)
        return brand_name
    except Exception as e:
        self.logger.error(f"Failed to apply brand filter: {e}
        raise

    def click_random_search_result(self):
        try: 
           links = self.util.wait_for_elements(self.product_links, 20)
           if not links:
                self.util.capture_screenshots("no_search_results")
                raise Exception
                
           chosen_link = random.choice(links)
           self.util.execute_script("arguments[0].scrollIntoView({behaviour: 'smooth', block: 'center'});", chosen_link)
           self.driver.execute_script("arguments[0].click();", chosen_link)
           time.sleep(3)
           if len(self.driver.window_handles) > 1:
              self.driver.switch_to.window(self.driver.window_handles[-1])
           
           self.logger.info("Random product clicked.")
           self.util.capture_screenshots("Random product clicked.")
        except Exception as e:
           self.logger.error(f"Failed to click random search result: {e}")
           raise

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

