import os

import pytest
from pages.common.login_page import LoginPage
from pages.PD.security_PD_page import SecurityPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestSecurity:

    def test_valid_file(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        #Perform profile preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)

        # Initialize the ProfilePage object with the driver instance
        security_page = SecurityPage(self.driver)

        # Perform profile actions
        security_page.click_security_module()
        security_page.click_add_keys_button()
        # Dynamically get the project root (assuming this script is in the 'tests' folder)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Resolve the file path from the project root
        file_path = os.path.join(project_root, 'resources/dummytest.txt')
        logger.info(file_path)
        security_page.enter_file_path(file_path)
        security_page.click_upload_file_button()

        # Assert and handle screenshot on failure
        assert security_page.get_success_message().is_displayed()

        take_screenshot(self.driver, "PGP_file_downloaded_successfully_screenshot")



    def test_invalid_file(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        #Perform profile preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)

        # Initialize the ProfilePage object with the driver instance
        security_page = SecurityPage(self.driver)

        # Perform profile actions
        security_page.click_security_module()
        security_page.click_add_keys_button()
        # Dynamically get the project root (assuming this script is in the 'tests' folder)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Resolve the file path from the project root
        file_path = os.path.join(project_root, 'resources/dummytest.txt')
        security_page.enter_file_path(file_path)

        security_page.click_upload_file_button()

        # Assert and handle screenshot on failure
        assert security_page.get_success_message().is_displayed()
        take_screenshot(self.driver, "PGP_file_downloaded_successfully_screenshot")
