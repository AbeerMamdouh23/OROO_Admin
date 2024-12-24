from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage

class SecurityPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    SECURITY_MODULE = (By.XPATH,  "//a[text()='Security']")
    UNAUTHORIZED_ACCESS_TEXT = (By.ID, "securityTop")



    def click_security_module(self):
            self.click(*self.SECURITY_MODULE)

    def get_unauthorized_text(self):
        return self.find_element(*self.UNAUTHORIZED_ACCESS_TEXT)
