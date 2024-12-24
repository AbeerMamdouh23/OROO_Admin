from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ChassisPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    CHASSIS_MODULE = (By.XPATH, "//a[text()='Chassis']")
    NO_CHASSIS_FOUNDED = (By.ID, "chassisInfoTableContainerText")
    CHASSIS_TABLE = (By.ID, "chassisInfoTable")




    def click_chassis_module(self):
            self.click(*self.CHASSIS_MODULE)

    def get_no_chassis_founded(self):
        return self.find_element(*self.NO_CHASSIS_FOUNDED)

    def get_view_chassis(self):
        try:

             elements= self.find_elements(*self.CHASSIS_TABLE)
             if len(elements) == 0:
                 return False
             else:
                 return  True
        except Exception:
            return False