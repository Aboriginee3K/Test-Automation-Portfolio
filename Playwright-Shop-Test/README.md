# Playwright E-Commerce Automation

# Overview
A modern, high-speed test automation script built with Microsoft Playwright. 
This project automates the critical "Add to Cart" user journey on SauceDemo(https://www.saucedemo.com/), demonstrating the advantages of Playwright over traditional tools like Selenium.

# Why Playwright?
Unlike older frameworks, this project utilizes Playwright's key features:
* Auto-Waiting: No need for 'time.sleep()' or explicit waits; Playwright waits for elements to be actionable automatically.
* Robust Locators: Uses user-facing locators like 'get_by_role' and 'get_by_text' instead of brittle XPaths.
* Speed: Runs significantly faster due to WebSocket communication (Headless by default).

# Tech Stack
* Python 3
* Playwright
* Pytest

# Test Scenarios
* File: 'test_shop.py'
1.  Login: Authenticate with standard credentials.
2.  Inventory: Locate specific products using text filters (not IDs).
3.  Add to Cart: dynamic interaction with buttons.
4.  Cart Verification: Validate item details in the shopping cart.

# How to Run
1.  Install Dependencies:
    '''pip install -r requirements.txt'''
2.  Install Browsers (Crucial step for Playwright):
    '''playwright install + browser'''
3.  Run Tests:
    Run in background (Headless):
    '''pytest'''
    Run with browser visible (Headed + Slow motion):
    '''pytest --headed --slowmo 500'''