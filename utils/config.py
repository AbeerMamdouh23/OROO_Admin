import os
import time

def take_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join("test-output","screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)




class Config:

    URL = "https://admin.dev-ooro.co.uk/"
    #STAGING_URL = ""
    PRODUCT_DIRECTOR_USERNAME_VALID = "ProductDirector"
    PRODUCT_DIRECTOR_PASSWORD_VALID = "productdirector"
    PRODUCT_DIRECTOR_USERNAME_INVALID = "productdirector"
    PRODUCT_DIRECTOR_PASSWORD_INVALID = "productdirector"
    ATE_MANAGER_USERNAME_VALID = "TestLead"
    ATE_MANAGER_PASSWORD_VALID = "testlead"
    ATE_MANAGER_USERNAME_INVALID = "TEST"
    ATE_MANAGER_PASSWORD_INVALID = "TEST"
    AUTHENTICATION_CODE = "000000"