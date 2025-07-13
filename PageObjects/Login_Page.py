from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPage:
    hover_signin = (By.ID, "nav-link-accountList")
    btn_signin_dropdown = (By.CSS_SELECTOR, "#nav-flyout-ya-signin a")
    textbox_email = (By.XPATH, "//input[@id='ap_email_login']")
    continue_btn = (By.ID, "continue")
    password_field = (By.ID, "ap_password")
    signin_btn = (By.ID, "signInSubmit")

    def __init__(self, driver, util):
        self.driver = driver
        self.util = util

    def login(self, username, password):
        self.util.hover_over_element(self.hover_signin)
        self.util.click_element(self.btn_signin_dropdown)
        self.util.send_keys(self.textbox_email, username)
        self.util.click_element(self.continue_btn)
        self.util.send_keys(self.password_field, password)
        self.util.click_element(self.signin_btn)
        self.util.capture_screenshot("after_login")
