import re
from playwright.sync_api import Page, expect


def test_add_to_cart(page: Page):
    """
    Test scenario: login
    """
    # 1. open page
    page.goto("https://www.saucedemo.com/")

    # 2. login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # 3. Expect login successful
    expect(page).to_have_title(re.compile("Swag Labs"))

    # 4. Add items to shopping cart
    page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button", name="Add to cart").click()

    # 5. Enter shopping cart
    page.locator(".shopping_cart_link").click()

    # 6. Assertion: is the Sauce Labs Backpack in the cart?
    cart_item = page.locator(".inventory_item_name")
    expect(cart_item).to_have_text("Sauce Labs Backpack")

    # screenshot for cart
    page.screenshot(path="cart_evidence.png")