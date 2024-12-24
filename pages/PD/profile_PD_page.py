from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_MODULE = (By.XPATH, "//a[text()='Profile']")
    PGP_KEYS_BUTTON = (By.ID, "profileTopButtonsRequestKeys")
    DOWNLOAD_FILE_BUTTON = (By.ID, "profileTopButtonsDownloadKeys")



    def click_profile_module(self):
            self.click(*self.PROFILE_MODULE)

    def click_PGP_button(self):
        self.click(*self.PGP_KEYS_BUTTON)

    def click_download_file_button(self):
        self.click(*self.DOWNLOAD_FILE_BUTTON)

    def get_download_file_button(self):
        return self.find_element(*self.DOWNLOAD_FILE_BUTTON)
