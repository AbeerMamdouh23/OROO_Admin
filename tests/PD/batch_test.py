import pytest
from pages.common.login_page import LoginPage
from pages.PD.batch_page import BatchPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestBatch:

    def test_existing_batches(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        #Perform chassis preconditions
        login_page.login_steps(Config.PRODUCT_DIRECTOR_USERNAME_VALID,Config.PRODUCT_DIRECTOR_PASSWORD_VALID)


        # Initialize the ChassisPage object with the driver instance
        batch_page = BatchPage(self.driver)

        # Perform chassis actions
        batch_page.click_model_module()
        batch_page.click_view_button()
        batch_page.click_see_batches()


        # Assert and handle screenshot on failure
        assert batch_page.get_view_batches() ==True

        take_screenshot(self.driver, "There_is_existing_batches_screenshot")
