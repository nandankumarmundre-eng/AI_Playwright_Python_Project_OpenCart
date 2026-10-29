from playwright.sync_api import Page, Locator

from pages.locators.search_locators import HomeSearchLocators
from utils.playwright_actions import execute_ui_action


class HomeSearchComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = HomeSearchLocators(page)

    def search(self, search_term: str) -> None:
        execute_ui_action(
            self.page,
            "fill in the product search field",
            lambda: self.locators.search_input.fill(search_term),
        )
        execute_ui_action(
            self.page,
            "submit the product search",
            self.locators.search_button.click,
        )
