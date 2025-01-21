import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage

class SecurityPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    SECURITY_MODULE = (By.XPATH,  "//a[text()='Security']")
    UNAUTHORIZED_ACCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Unauthorized access')]")


    @allure.step("Click security module")
    def click_security_module(self):
        self.click(*self.SECURITY_MODULE)
        return self


    @allure.step("Unauthorized access")
    def get_unauthorized_text(self):
        return self.find_element(*self.UNAUTHORIZED_ACCESS_TEXT)


    @allure.step("Success Unauthorized Access")
    def assert_success_unauthorized(self):
        assert self.assert_on_unauthorized_text() == True
        return self

    @allure.step("Fail Unauthorized Access")
    def assert_fail_unauthorized(self):
        assert self.assert_on_unauthorized_text() == False
        return self

    def assert_on_unauthorized_text(self):
        try:
            return self.get_unauthorized_text().is_displayed()
        except Exception:
            return False