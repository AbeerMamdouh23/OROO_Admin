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

    def click_model_module(self):
            self.click(*self.MODEL_MODULE)

    def click_view_button(self):
            self.click(*self.VIEW_BUTTON)

    def click_see_batches(self):
            self.click(*self.BATCH_BUTTON)

    def get_no_batch_founded(self):
        return self.find_element(*self.NO_BATCH_FOUNDED)

    def get_view_batches(self):
        try:
            self.find_element(*self.VIEW_BATCHES)
            return True
        except Exception:
            return False
