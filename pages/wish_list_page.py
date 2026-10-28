from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.locators.account_wishlist_locators import AccountWishListLocators


class WishListPage(BasePage):
    def __init__(self, page: Page, product_name: str) -> None:
        super().__init__(page)
        self.locators = AccountWishListLocators(page, product_name)

    @property
    def product_row(self) -> Locator:
        return self.locators.product_row

    @property
    def empty_wish_list_message(self) -> Locator:
        return self.locators.empty_wish_list_message

    def remove_item(self) -> None:
        self.locators.remove_item_button.click()
    