import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class BatchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    MODEL_MODULE = (By.XPATH, "//a[text()='Models']")
    VIEW_BUTTON = (By.XPATH, "(//*[@id='modelTableBodyViewButton'])[1]")
    BATCH_BUTTON = (By.ID, "modelIDTopViewBatchButton")
    NO_BATCH_FOUNDED = (By.XPATH, "//p[contains(text(), 'No batches found')]")
    VIEW_BATCHES = (By.ID, "batchesTableTopRowUUID")



    @allure.step("Click Models module")
    def click_model_module(self):
        self.click(*self.MODEL_MODULE)
        return self


    @allure.step("Click View button")
    def click_view_button(self):
        self.click(*self.VIEW_BUTTON)
        return self


    @allure.step("Click see batches button")
    def click_see_batches(self):
        self.click(*self.BATCH_BUTTON)
        return self

    def get_view_batches(self):
        try:
            elements = self.find_element(*self.VIEW_BATCHES)
            if len(elements) == 0:
                return False
            else:
                return True
        except Exception:
            return False


    @allure.step("No batches founded")
    def assert_No_batches_founded(self):
        assert self.get_view_batches() == False
        return self


    @allure.step("Existing chassis successfully")
    def assert_existing_batches(self):
        assert self.get_view_batches() == True
        return self
