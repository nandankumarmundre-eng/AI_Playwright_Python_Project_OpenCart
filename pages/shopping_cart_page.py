from playwright.sync_api import Locator, Page

from pages.locators.shopping_cart_locators import ShoppingCartLocators
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page, product_name: str) -> None:
        super().__init__(page)
        self.locators = ShoppingCartLocators(page, product_name)

    @property
    def heading(self) -> Locator:
        return self.locators.heading

    @property
    def product_row(self) -> Locator:
        return self.locators.product_row
