from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_product(page: Page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Verify product page
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Add products
    product_page.add_backpack()
    product_page.add_bike_light()

    # Verify cart count
    expect(product_page.cart_badge).to_have_text("2")

    # Open cart
    product_page.open_cart()

    # Verify cart
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    # Checkout
    product_page.checkout()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    # Fill details
    product_page.enter_details(
        "megha",
        "naaa",
        "23456543q"
    )

    # Continue
    product_page.continue_checkout()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )

    # Finish
    product_page.finish_order()

    # Verify success
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )

    expect(
        page.get_by_role(
            "heading",
            name="Thank you for your order!"
        )
    ).to_be_visible()