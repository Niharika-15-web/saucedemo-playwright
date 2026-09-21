from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        self.url = ("https://www.saucedemo.com/")

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button" , name = "Login")

    def open(self):
             self.page.goto(self.url)


    def login(self, username , password):
            self.username.fill("standard_user")
            self.password.fill("secret_sauce")
            self.login_button.click()

