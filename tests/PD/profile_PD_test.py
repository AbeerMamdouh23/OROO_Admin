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
        login_page = LoginPage(self.driver)

        #Perform profile preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)

        # Initialize the ProfilePage object with the driver instance
        profile_page = ProfilePage(self.driver)

        # Perform profile actions
        profile_page.click_profile_module()
        profile_page.click_PGP_button()
        profile_page.click_download_file_button()

        # Assert and handle screenshot on failure
        assert profile_page.get_download_file_button().is_displayed()

        take_screenshot(self.driver, "PGP_file_downloaded_successfully_screenshot")
