import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class SecurityPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    SECURITY_MODULE = (By.XPATH, "//a[text()='Security']")
    ADD_KEYS_BUTTON = (By.ID, "securityGenericTableBodyAddKeysButton")
    CHOOSE_FILE_BUTTON = (By.ID, "addFileFile")
    UPLOAD_FILE_BUTTON = (By.ID, "addFileUploadButton")
    SUCCESS_UPLOADED_MESSAGE = (By.ID, "changePasswordMessage")
    #ERROR_UPLOADED_MESSAGE = (By.ID, "")



    @allure.step("Click security module")
    def click_security_module(self):
        self.click(*self.SECURITY_MODULE)
        return self


    @allure.step("Click add keys button")
    def click_add_keys_button(self):
        self.click(*self.ADD_KEYS_BUTTON)
        return self

    @allure.step("Click choose file button")
    def click_choose_file_button(self):
        self.click(*self.CHOOSE_FILE_BUTTON)
        return self

    @allure.step("Click upload button")
    def click_upload_file_button(self):
        self.click(*self.UPLOAD_FILE_BUTTON)
        return self

    @allure.step("Choose file")
    def enter_file_path(self , file_path):
        self.send_text(file_path, *self.CHOOSE_FILE_BUTTON)
        return self

    @allure.step("Success upload message")
    def get_success_message(self):
        return self.find_element(*self.SUCCESS_UPLOADED_MESSAGE)


    @allure.step("Success Unauthorized Access")
    def assert_success_uploaded(self):
        assert self.assert_on_success_uploaded() == True
        return self

    @allure.step("Fail Unauthorized Access")
    def assert_fail_uploaded(self):
        assert self.assert_on_success_uploaded() == False
        return self

    def assert_on_success_uploaded(self):
        try:
            return self.get_success_message().is_displayed()
        except Exception:
            return False


    #def get_error_message(self):
    #    return self.find_element(*self.ERROR_UPLOADED_MESSAGE)
