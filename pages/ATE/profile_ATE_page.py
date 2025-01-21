import allure
from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_MODULE = (By.XPATH, "//a[text()='Profile']")
    PGP_KEYS_BUTTON = (By.ID, "profileTopButtonsRequestKeys")


    @allure.step("Click Profile module")
    def click_profile_module(self):
        self.click(*self.PROFILE_MODULE)
        return self


    @allure.step("Get PGP button")
    def get_PGP_button(self):
        try:
              elements =  self.find_elements(*self.PGP_KEYS_BUTTON).is_displayed()
              if len(elements) == 0:
                  return False
              else:
                  return True
        except Exception:
              return False

    @allure.step("Success display download file button")
    def assert_success_display_download_file(self):
        assert self.get_PGP_button() == True
        return self

    @allure.step("Fail display download file button")
    def assert_fail_display_download_file(self):
        assert self.get_PGP_button() == False
        return self
