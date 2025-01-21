import allure
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


    @allure.step("Enter User Name")
    def enter_username(self, email):
        self.send_text(email, *self.USERNAME_FIELD)
        return self


    @allure.step("Enter Password")
    def enter_password(self, password):
        self.send_text(password, *self.PASSWORD_FIELD)
        return self


    @allure.step("Click on login button")
    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)
        return self


    def login_steps(self,email,password):
        self.send_text(email, *self.USERNAME_FIELD)
        self.send_text(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)
        return self


    @allure.step("Validate success login ")
    def assert_success_login(self):
        assert self.assert_on_login() == False
        return self

    @allure.step("Validate fail login ")
    def assert_fail_login(self):
        assert self.assert_on_login() == True
        return self

    def assert_on_login(self):
        try:
            return self.get_error_message().is_displayed()
        except Exception:
            return False

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE)


    def get_dashboard_text(self):
        return self.find_element(*self.DASHBOARD_TEXT)



    #def enter_auth_code(self, authcode):
    #    self.send_text(authcode, *self.AUTHCODE_FIELD)


    #def click_verify_button(self):
    #   self.click(*self.VERIFY_BUTTON)
