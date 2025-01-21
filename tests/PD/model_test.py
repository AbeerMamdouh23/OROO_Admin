
import pytest
from pages.common.login_page import LoginPage
from pages.PD.model_page import ModelPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestModel:

    # TODO: Refactor test_existing_model test case in case modifying the performance
    def test_existing_model(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID, Config.PRODUCT_DIRECTOR_PASSWORD_VALID)
         .assert_success_login())

        # Initialize the ModelPage object with the driver instance
        (ModelPage(self.driver)
         .click_model_module()
         .assert_existing_models())

        take_screenshot(self.driver, "There_is_existing_models_screenshot")
