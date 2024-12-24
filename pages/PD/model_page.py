from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ModelPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    MODEL_MODULE = (By.XPATH, "//a[text()='Models']")
    VIEW_MODELS = (By.ID, "modelTable")
    NO_MODEL_FOUNDED = (By.ID, "")



    def click_model_module(self):
            self.click(*self.MODEL_MODULE)

    def get_view_models(self):
        elements= self.find_elements(*self.VIEW_MODELS)
        if len(elements) == 0:
            return False
        else:
            return True

    #def get_no_model_founded(self):
    #    return self.find_element(*self.NO_MODEL_FOUNDED)
