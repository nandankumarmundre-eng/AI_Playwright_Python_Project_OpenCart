from playwright.sync_api import Locator, Page

from data.web.models import LoginCredentials
from pages.locators.login_locators import LoginLocators
from pages.base_page import BasePage
from utils.playwright_actions import execute_ui_action


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = LoginLocators(page)

    @property
    def account_heading(self) -> Locator:
        return self.locators.account_heading

    def login(self, credentials: LoginCredentials) -> None:
        execute_ui_action(
            self.page,
            "fill in the login email",
            lambda: self.locators.email.fill(credentials.email),
        )
        execute_ui_action(
            self.page,
            "fill in the login password",
            lambda: self.locators.password.fill(credentials.password),
        )
        execute_ui_action(
            self.page,
            "submit the login form",
            self.locators.login_button.click,
        )
