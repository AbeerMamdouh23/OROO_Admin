import pytest

from pages.common.login_page import LoginPage
from pages.common.logout_page import LogOutPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogout:

    def test_logout(self, setup):

        self.driver = setup  # Assign the driver from the fixture


        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        #Perform Login preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)

        # Initialize the LogOutPage object with the driver instance
        logout_page = LogOutPage(self.driver)

        # Perform logout action
        logout_page.click_logout_button()

        # Assert and handle screenshot on failure
        assert  logout_page.get_login_page().is_displayed()
        take_screenshot(self.driver, "logout_screenshot")
