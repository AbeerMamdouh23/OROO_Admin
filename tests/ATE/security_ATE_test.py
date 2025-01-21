import pytest

from pages.common.login_page import LoginPage
from pages.ATE.security_ATE_page import SecurityPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestSecurity:

    def test_security(self, setup):

        self.driver = setup  # Assign the driver from the fixture


        #Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.ATE_MANAGER_USERNAME_VALID, Config.ATE_MANAGER_PASSWORD_VALID)
         .assert_success_login())

        #Initialize the SecurityPage object with the driver instance
        (SecurityPage(self.driver)
         .click_security_module()
         .assert_success_unauthorized())

        #Assert and handle screenshot on failure
        take_screenshot(self.driver, "Unauthorized_access_screenshot")