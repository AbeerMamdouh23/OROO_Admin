import pytest

from pages.common.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogin:

    # Test case for valid login with correct credentials
    def test_valid_login(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver).enter_username(Config.PRODUCT_DIRECTOR_USERNAME_VALID)
         .enter_password(Config.PRODUCT_DIRECTOR_PASSWORD_VALID)
         .click_login_button()
         .assert_success_login())
        take_screenshot(self.driver, "valid_login_screenshot")


    # Test case for invalid login with incorrect credentials using explicit wait
    def test_invalid_login(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver).enter_username(Config.PRODUCT_DIRECTOR_USERNAME_INVALID)
         .enter_password(Config.PRODUCT_DIRECTOR_PASSWORD_INVALID)
         .click_login_button()
         .assert_fail_login())
        take_screenshot(self.driver, "Invalid_login_screenshot")
