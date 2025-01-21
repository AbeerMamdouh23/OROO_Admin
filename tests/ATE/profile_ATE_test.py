from cProfile import Profile

import pytest
from pages.common.login_page import LoginPage
from pages.ATE.profile_ATE_page import ProfilePage
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
         .login_steps(Config.ATE_MANAGER_USERNAME_VALID, Config.ATE_MANAGER_PASSWORD_VALID)
        .assert_success_login())


        # Initialize the ProfilePage object with the driver instance
        (ProfilePage(self.driver)
         .click_profile_module()
         .assert_success_display_download_file())

        take_screenshot(self.driver, "PGP_keys_button_not_existing_screenshot")
