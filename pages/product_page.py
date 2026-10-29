from playwright.sync_api import Locator, Page

from pages.locators.product_locators import ProductLocators
from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCartPage
from pages.wish_list_page import WishListPage
from utils.playwright_actions import execute_ui_action


class ProductPage(BasePage):
    def __init__(self, page: Page, product_name: str) -> None:
        super().__init__(page)
        self.product_name = product_name
        self.locators = ProductLocators(page, product_name)

    @property
    def product_heading(self) -> Locator:
        return self.locators.product_heading

    @property
    def add_to_cart_success(self) -> Locator:
        return self.locators.add_to_cart_success

    def add_to_cart(self) -> "ProductPage":
        execute_ui_action(
            self.page,
            f"add {self.product_name} to the cart",
            self.locators.add_to_cart_button.click,
        )
        return self

    def open_shopping_cart(self) -> ShoppingCartPage:
        execute_ui_action(
            self.page,
            "open the shopping cart from the success message",
            self.locators.shopping_cart_link.click,
        )
        return ShoppingCartPage(self.page, self.product_name)

    def add_to_wish_list(self) -> "ProductPage":
        execute_ui_action(
            self.page,
            f"add {self.product_name} to the wish list",
            self.locators.add_to_wish_list_button.click,
        )
        return self

    def add_to_wish_list_success(self) -> Locator:
        return self.locators.add_to_wish_list_success

    def wish_list_product_link(self) -> Locator:
        return self.locators.wish_list_product_link

    def wish_list_link(self) -> Locator:
        return self.locators.wish_list_link

    def open_wish_list(self) -> "WishListPage":
        execute_ui_action(
            self.page,
            "open the wish list from the success message",
            self.locators.wish_list_link.click,
        )
        return WishListPage(self.page, self.product_name)
    