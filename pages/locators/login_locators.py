from playwright.sync_api import Locator, Page


class LoginLocators:
    EMAIL_PLACEHOLDER = "E-Mail Address"
    PASSWORD_PLACEHOLDER = "Password"

    def __init__(self, page: Page) -> None:
        self.email: Locator = page.get_by_placeholder(
            self.EMAIL_PLACEHOLDER, exact=True
        )
        self.password: Locator = page.get_by_placeholder(
            self.PASSWORD_PLACEHOLDER, exact=True
        )
        self.login_button: Locator = page.get_by_role(
            "button", name="Login", exact=True
        )
        self.account_heading: Locator = page.get_by_role(
            "heading", name="My Account", level=2, exact=True
        )
