import pytest
from pages.common.login_page import LoginPage
from pages.PD.profile_PD_page import ProfilePage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestProfile:

    def test_profile(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID, Config.PRODUCT_DIRECTOR_PASSWORD_VALID)
         .assert_success_login())

        # Initialize the ProfilePage object with the driver instance
        (ProfilePage(self.driver)
         .click_profile_module()
         .click_PGP_button()
         .assert_success_display_download_file_button())

        take_screenshot(self.driver, "PGP_file_downloaded_successfully_screenshot")
