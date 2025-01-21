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
        (LoginPage(self.driver)
         .login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID, Config.PRODUCT_DIRECTOR_PASSWORD_VALID)
         .assert_success_login())

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Resolve the file path from the project root
        file_path = os.path.join(project_root, 'resources/dummytest.txt')
        logger.info(file_path)
        (SecurityPage(self.driver)
         .click_security_module()
         .click_add_keys_button()
         .enter_file_path(file_path)
         .click_upload_file_button()
         .assert_on_success_uploaded())

        # Assert and handle screenshot on failure
        take_screenshot(self.driver, "Keys_uploaded_successfully_screenshot")



    def test_invalid_file(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID, Config.PRODUCT_DIRECTOR_PASSWORD_VALID)
         .assert_success_login())

        # Initialize the ProfilePage object with the driver instance
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Resolve the file path from the project root
        file_path = os.path.join(project_root, 'resources/dummytest.txt')
        logger.info(file_path)
        (SecurityPage(self.driver)
         .click_security_module()
         .click_add_keys_button()
         .enter_file_path(file_path)
         .click_upload_file_button()
         .assert_on_success_uploaded())

        take_screenshot(self.driver, "Keys_not uploaded_successfully_screenshot")
