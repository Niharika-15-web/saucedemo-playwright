from playwright.sync_api import Page,expect
from pages.login_page import LoginPage

def test_login(page:Page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Swag Labs")).to_be_visible()
