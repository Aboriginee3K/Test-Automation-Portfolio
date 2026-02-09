import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Login Functionality")
class TestLogin:

    @allure.story("Successful Login")
    def test_valid_login(self, driver):
        # 1. initialize the page
        login_page = LoginPage(driver)

        # 2. open the page
        login_page.load()

        # 3. action: login with correct username and password
        login_page.login("standard_user", "secret_sauce")

        # 4. Assertion: login successful or not
        assert login_page.is_logo_displayed() == True

    @allure.story("Failed Login - Locked Out User")
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()

        # use locked out username and password
        login_page.login("locked_out_user", "secret_sauce")

        # Assertion: if the error text displayed correctly
        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text

    @allure.story("Failed Login - Invalid Credentials")
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()

        # use wrong username and password
        login_page.login("wrong_user", "wrong_pass")

        # Assertion: if the error text displayed correctly
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text