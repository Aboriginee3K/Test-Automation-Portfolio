# Web UI Automation Framework

# Overview
A robust automation framework designed to test the login functionality of SauceDemo(https://www.saucedemo.com/). 

Built using the Page Object Model (POM) design pattern to ensure maintainability and scalability. This project demonstrates my ability to structure automated tests professionally, separating test logic from page mechanics.

# Tech Stack
* Python
* Selenium WebDriver (Browser Automation)
* Pytest (Test Runner)
* Allure (Reporting)
* Page Object Model

# Project Structure
* ‘pages/’: Contains Page Object classes (Locators & Methods).
* ‘tests/’: Contains actual test scripts using Pytest.
* ‘conftest.py’: Manages WebDriver fixtures (Setup/Teardown).

# How to Run
1. Install dependencies:
   '''pip install -r requirements.txt'''
2. Run tests:
   '''pytest test/test_login.py'''
3. Generate Allure Report(Optional):
   '''pytest --alluredir=reports
      allure serve reports'''