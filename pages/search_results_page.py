from playwright.sync_api import Locator, Page

from pages.locators.search_locators import SearchResultsLocators
from pages.base_page import BasePage
from pages.product_page import ProductPage
from utils.playwright_actions import execute_ui_action


class SearchResultsPage(BasePage):
    def __init__(self, page: Page, search_term: str) -> None:
        super().__init__(page)
        self.locators = SearchResultsLocators(page, search_term)

    @property
    def search_heading(self) -> Locator:
        return self.locators.search_heading

    @property
    def first_product_card(self) -> Locator:
        return self.locators.product_cards.first

    def product_heading(self, product_name: str) -> Locator:
        return self.locators.product_heading(product_name)

    def open_product(self, product_name: str) -> ProductPage:
        execute_ui_action(
            self.page,
            f"open the {product_name} product",
            self.locators.product_link(product_name).click,
        )
        return ProductPage(self.page, product_name)
