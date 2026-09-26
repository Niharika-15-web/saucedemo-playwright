from playwright.async_api import Page,expect

class ProductsPage():

    def __init__ (self,page:Page):
        self.page = Page

        self.backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.Bike_light = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.Bolt_tshirt = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.cart = page.locator(".shopping_cart_link")
        self.menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")



    def add_backpack(self):
        self.backpack.click()

    def add_bike_light(self):
        self.Bike_light.click()

    def add_bolt_tshirt(self):
        self.Bolt_tshirt.click()

    def open_cart(self):
        self.cart.click()

    def logout(self):
        self.menu.click()
        self.logout_link.click()