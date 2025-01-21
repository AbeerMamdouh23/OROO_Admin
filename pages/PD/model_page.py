import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ModelPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    MODEL_MODULE = (By.XPATH, "//a[text()='Models']")
    VIEW_MODELS = (By.ID, "modelTable")


    @allure.step("Click Models module")
    def click_model_module(self):
        self.click(*self.MODEL_MODULE)
        return self


    def get_view_models(self):
        try:
            elements= self.find_elements(*self.VIEW_MODELS)
            if len(elements) == 0:
                return False
            else:
                return True
        except Exception:
            return False



    @allure.step("No Models founded")
    def assert_No_models_founded(self):
        assert self.get_view_models() == False
        return self


    @allure.step("Existing models successfully")
    def assert_existing_models(self):
        assert self.get_view_models() == True
        return self
