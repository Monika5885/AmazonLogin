import random
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Checkout_Page:
    account_menu_id = "nav-link-accountList"
    Checkout_xpath = "//span[@id='sc-buy-box-ptc-button']"
    Address_xpath = "(//span[@class='a-button-inner']) [2]"
    selected_address_xpath = "//span[@id='deliver-to-address-text']"
    Payment_Credit_Debit_Card_xpath = "//input[@id='pp-ugd9Zl-101']"
    Payment_Net_Banking_xpath = "//input[@id='pp-ugd9Z1-107']"
    Payment_EMI_xpath = "//span[contains (text(),'EMI')]"

    def _init_(self, driver, util):
        self.driver = driver
        self.util = util
        self.logger = logging.getLogger(__name__)

    def click_account_menu(self):
        self.driver.find_element(By.ID, self.account_menu_id).click()

    def click_Checkout(self):
        self.driver.find_element(By.XPATH, self.Checkout_xpath).click()

    def Select_Address(self):
        self.driver.find_element(By.XPATH, self.Address_xpath).click()




