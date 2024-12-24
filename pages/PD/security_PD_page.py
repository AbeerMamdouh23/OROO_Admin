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




    def click_security_module(self):
            self.click(*self.SECURITY_MODULE)

    def click_add_keys_button(self):
        self.click(*self.ADD_KEYS_BUTTON)

    def click_choose_file_button(self):
        self.click(*self.CHOOSE_FILE_BUTTON)

    def click_upload_file_button(self):
        self.click(*self.UPLOAD_FILE_BUTTON)

    def enter_file_path(self , file_path):
        self.send_text(file_path, *self.CHOOSE_FILE_BUTTON)

    def get_success_message(self):
        return self.find_element(*self.SUCCESS_UPLOADED_MESSAGE)

    #def get_error_message(self):
    #    return self.find_element(*self.ERROR_UPLOADED_MESSAGE)
