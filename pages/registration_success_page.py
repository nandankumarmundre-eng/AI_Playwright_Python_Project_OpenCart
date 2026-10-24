from playwright.sync_api import Locator, Page

from pages.locators.account_locators import AccountLocators
from pages.base_page import BasePage


class RegistrationSuccessPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = AccountLocators(page)

    @property
    def created_heading(self) -> Locator:
        return self.locators.created_heading
