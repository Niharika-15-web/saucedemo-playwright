from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page:Page):
         self.page = page

         self.firstname = page.get_by_placeholder("First Name")
         self.lastname = page.get_by_placeholder("Last Name")
         self.zipcode = page.get_by_placeholder("Zip/Postal Code")
         self.continue_button = page.get_by_role("button", name = "continue")
         self.finish_button = page.get_by_role("button", name = "finish")
         self.checkout_complete = page.get_by_text("Thank you for your order!")


    def enter_checkout_details(self, firstname, lastname, zipcode):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.zipcode.fill(zipcode)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checko(self):
        self.finish_button.click()
