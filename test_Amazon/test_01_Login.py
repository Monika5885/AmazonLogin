import pytest
from PageObjects.Login_Page import LoginPage
from Utilities.Reusable_Method import ReusableMethod

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_amazon(self, config):
        util = ReusableMethod(self.driver)
        try:
            login = LoginPage(self.driver, util)
            login.login(util.get_username(config),util.get_password(config))
            util.capture_screenshot("Login_success")
        except Exception as e:
             util.capture_screenshot("Login_fail")
             raise e

