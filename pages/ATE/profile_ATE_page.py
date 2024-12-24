from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_MODULE = (By.XPATH, "//a[text()='Profile']")
    PGP_KEYS_BUTTON = (By.ID, "profileTopButtonsRequestKeys")


    def click_profile_module(self):
            self.click(*self.PROFILE_MODULE)

    def get_PGP_button(self):
        try:
              elements =  self.find_elements(*self.PGP_KEYS_BUTTON)
              if len(elements) == 0:
                  return False
              else:
                  return True
        except Exception:
            return False

