from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


def test_checkout(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack()
    products_page.add_bolt_tshirt()
    products_page.add_bike_light()

    products_page.open_cart()

    expect(cart_page.backpack).to_be_visible()
    expect(cart_page.bike_light).to_be_visible()
    expect(cart_page.bolt_tshirt).to_be_visible()

    cart_page.checkout()

    checkout_page.enter_checkout_details(
        "Megha",
        "Nair",
        "530001"
    )

    checkout_page.continue_checkout()

    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    checkout_page.finish_button.click()

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )