import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ChassisPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    CHASSIS_MODULE = (By.XPATH, "//a[text()='Chassis']")
    NO_CHASSIS_FOUNDED = (By.ID, "chassisInfoTableContainerText")
    CHASSIS_TABLE = (By.ID, "chassisInfoTable")



    @allure.step("Click Chassis module")
    def click_chassis_module(self):
        self.click(*self.CHASSIS_MODULE)
        return self


    def get_view_chassis(self):
        try:
             elements= self.find_elements(*self.CHASSIS_TABLE)
             if len(elements) == 0:
                 return False
             else:
                 return  True
        except Exception:
            return False


    @allure.step("No chassis founded")
    def assert_No_chassis_founded(self):
        assert self.get_view_chassis() == False
        return self


    @allure.step("Existing chassis successfully")
    def assert_existing_chassis(self):
        assert self.get_view_chassis() == True
        return self
