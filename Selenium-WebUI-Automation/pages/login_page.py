from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """open the login page"""
        self.driver.get(self.URL)

    def login(self, username, password):
        """login to saucedemo"""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Get error message"""
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_logo_displayed(self):
        """If successfully logged in"""
        return self.driver.find_element(*self.APP_LOGO).is_displayed()