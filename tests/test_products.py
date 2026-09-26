from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_products(page):
     login_page = LoginPage(page)
     products_page = ProductsPage(page)


     page.goto("https://www.saucedemo.com/")
     login_page.login("standard_user", "secret_sauce")


     products_page.add_backpack()
     products_page.add_bike_light()
     products_page.add_bolt_tshirt()