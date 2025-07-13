import os
from configparser import ConfigParser
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ReusableMethod:
    def __init__(self, driver):
            self.driver = driver
            # Load config when class is initialized
            self.config = ConfigParser()
            self.config.read(os.path.join(os.getcwd(), "configuration", "config.ini"))

    def get_config(self, section, key):
            return self.config.get(section, key)

    @staticmethod
    def get_application_url(config):
        return config.get('Common Info', 'baseurl')

    @staticmethod
    def get_username(config):
        return config.get('Common Info', 'username')

    @staticmethod
    def get_password(config):
        return config.get('Common Info', 'password')

    def send_keys(self, locator, value):
        self.wait_for_element(locator).clear()
        self.wait_for_element(locator).send_keys(value)

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.capture_screenshots("element not found")
            return []

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def select_dropdown_by_index(self, locator, index):
        element = self.driver.find_element(*locator)

    def get_text(self, locator):
        return self.wait_for_element(locator).text
        self.capture_screenshot(f"gettext_{locator[1]}")

    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        self.capture_screenshot(f"hover_{locator[1]}")

    def capture_screenshot(self, name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filepath)
        return filepath

    def quit(self):
        self.driver.quit()
        print("Browser closed")

