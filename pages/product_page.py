from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        # URL
        self.url = "https://www.saucedemo.com/inventory.html"

        # Products
        self.back_pack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")

        # Cart
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

        # Checkout
        self.checkout_button = page.get_by_role("button", name="Checkout")

        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")

        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")

    # Product actions
    def add_backpack(self):
        self.back_pack.click()

    def add_bike_light(self):
        self.bike_light.click()

    # Cart action
    def open_cart(self):
        self.cart_link.click()

    # Checkout actions
    def checkout(self):
        self.checkout_button.click()

    def enter_details(self, first_name, last_name, zip_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()