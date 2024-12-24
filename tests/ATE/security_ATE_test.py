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
        login_page = LoginPage(self.driver)

        #Perform Login preconditions
        login_page.login_steps(Config.ATE_MANAGER_USERNAME_VALID,Config.ATE_MANAGER_PASSWORD_VALID)

        #Initialize the SecurityPage object with the driver instance
        security_page = SecurityPage(self.driver)

        #Perform security actions
        security_page.click_security_module()

        #Assert and handle screenshot on failure
        assert security_page.get_unauthorized_text().is_displayed()
        take_screenshot(self.driver, "Unauthorized_access_screenshot")