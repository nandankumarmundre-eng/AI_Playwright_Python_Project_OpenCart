from playwright.sync_api import Page

from pages.locators.account_locators import AccountLocators
from pages.base_page import BasePage


class RegistrationSuccessPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = AccountLocators(page)
