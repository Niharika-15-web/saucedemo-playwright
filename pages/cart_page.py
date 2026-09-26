from playwright.sync_api import Page

class CartPage():

    def __init__ (self,page:Page):
        self.page = page

        self.backpack = page.get_by_text("Sauce Labs Backpack")
        self.bike_light = page.get_by_text("Sauce Labs Bike Light")
        self.bolt_tshirt = page.locator("[data-test='item-1-title-link']")
        self.checkout_button = page.get_by_role("button", name = "Checkout")

    def verify_backpack(self):
        return self.backpack

    def verify_bike_light(self):
        return self.bike_light

    def verify_bolt_tshirt(self):
        return self.bolt_tshirt

    def checkout(self):
        self.checkout_button.click()