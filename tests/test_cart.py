from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import Page,expect


def test_cart(page):

        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        cart_page = CartPage(page)

        page.goto("https://www.saucedemo.com/")

        login_page.login("standard_user", "secret_sauce")

        products_page.add_backpack()
        products_page.add_bike_light()
        products_page.add_bolt_tshirt()

        products_page.open_cart()

        expect(cart_page.backpack).to_be_visible()
        expect(cart_page.bike_light).to_be_visible()
        expect(cart_page.bolt_tshirt).to_be_visible()

        cart_page.checkout()


