from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    USERNAME_FIELD = (By.ID, "loginFormUsername")
    PASSWORD_FIELD = (By.ID, "loginFormPassword")
    LOGIN_BUTTON = (By.ID, "loginFormButton")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Invalid credentials')]")
    DASHBOARD_TEXT = (By.ID, "navbarTitle")
    #AUTHCODE_FIELD = (By.ID, "2FAFormInput")
    #VERIFY_BUTTON = (By.ID, "2FAVerifyButton")



    def enter_username(self, email):
        self.send_text(email, *self.USERNAME_FIELD)


    def enter_password(self, password):
        self.send_text(password, *self.PASSWORD_FIELD)


    #def enter_auth_code(self, authcode):
    #    self.send_text(authcode, *self.AUTHCODE_FIELD)


    #def click_login_button(self):
    #    self.click(*self.LOGIN_BUTTON)


    #def click_verify_button(self):
    #   self.click(*self.VERIFY_BUTTON)


    def login_steps(self,email,password):
        self.send_text(email, *self.USERNAME_FIELD)
        self.send_text(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)



    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)


    def get_dashboard_text(self):
        return self.find_element(*self.DASHBOARD_TEXT)
