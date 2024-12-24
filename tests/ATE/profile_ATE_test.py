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
        login_page = LoginPage(self.driver)

        #Perform Login preconditions
        login_page.login_steps(Config.ATE_MANAGER_USERNAME_VALID,Config.ATE_MANAGER_PASSWORD_VALID)

        # Initialize the ProfilePage object with the driver instance
        profile_page = ProfilePage(self.driver)

        # click on profile module
        profile_page.click_profile_module()

        # Assert and handle screenshot on failure
        assert  profile_page.get_PGP_button() == False

        take_screenshot(self.driver, "PGP_keys_button_not_existing_screenshot")
