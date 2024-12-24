import pytest
from pages.common.login_page import LoginPage
from pages.PD.chassis_page import ChassisPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestChassis:

    def test_existing_chassis(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        #Perform chassis preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)

        # Initialize the ChassisPage object with the driver instance
        chassis_page = ChassisPage(self.driver)

        # Perform chassis actions
        chassis_page.click_chassis_module()

        # Assert and handle screenshot on failure
        assert chassis_page.get_view_chassis() == True

        take_screenshot(self.driver, "There_is_existing_chassis_screenshot")
