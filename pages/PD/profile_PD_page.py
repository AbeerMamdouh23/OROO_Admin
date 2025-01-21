import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_MODULE = (By.XPATH, "//a[text()='Profile']")
    PGP_KEYS_BUTTON = (By.ID, "profileTopButtonsRequestKeys")
    DOWNLOAD_FILE_BUTTON = (By.ID, "profileTopButtonsDownloadKeys")


    @allure.step("Click Profile module")
    def click_profile_module(self):
        self.click(*self.PROFILE_MODULE)
        return self

    @allure.step("Click PGP button")
    def click_PGP_button(self):
        self.click(*self.PGP_KEYS_BUTTON)
        return self

    @allure.step("Click download file button")
    def click_download_file_button(self):
        self.click(*self.DOWNLOAD_FILE_BUTTON)
        return self

    def get_download_file_button(self):
        return self.find_element(*self.DOWNLOAD_FILE_BUTTON)

    @allure.step("Get PGP button")
    def get_download_file_button(self):
        try:
            elements = self.find_elements(*self.PGP_KEYS_BUTTON).is_displayed()
            if len(elements) == 0:
                return False
            else:
                return True
        except Exception:
            return False

    @allure.step("Success display download ")
    def assert_success_display_download_file_button(self):
        assert self.get_download_file_button() == True
        return self

    @allure.step("Fail display download file")
    def assert_fail_display_download_file_button(self):
        assert self.get_download_file_button() == False
        return self
