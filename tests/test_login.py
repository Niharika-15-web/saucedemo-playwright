from pages.login_page import LoginPage
from playwright.sync_api import Page,expect

def test_valid_login(page):
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

def test_invalid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("Invalid_user", "Invalid_password")
    expect(page.locator('[data-test="error-button"]')).to_be_visible()
