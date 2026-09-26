from playwright.sync_api import Page,expect

class LoginPage:

    def __init__(self,page:Page):
        self.page = page

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name = "Login")

        self.error_msg = page.locator('["data-test="error-button"]')

    def login(self,username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()