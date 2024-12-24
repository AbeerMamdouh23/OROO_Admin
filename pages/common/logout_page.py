from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class LogOutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    LOG_OUT_BUTTON = (By.ID, "sidebarLogOutButton")
    LOGIN_BUTTON = (By.ID, "loginFormButton")
    #AUTHCODE_FIELD = (By.ID, "2FAFormInput")
    #VERIFY_BUTTON = (By.ID, "2FAVerifyButton")



    def click_logout_button(self):
        self.click(*self.LOG_OUT_BUTTON)


    def get_login_page(self):
        return self.find_element(*self.LOGIN_BUTTON)

    #def enter_auth_code(self, authcode):
    #    self.send_text(authcode, *self.AUTHCODE_FIELD)


    #def click_verify_button(self):
    #    self.click(*self.VERIFY_BUTTON)







