from urllib.parse import urljoin

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.locators.account_wishlist_locators import AccountWishListLocators
from utils.playwright_actions import execute_ui_action


class WishListPage(BasePage):
    WISH_LIST_PATH = "index.php?route=account/wishlist"

    def __init__(
        self, page: Page, product_name: str, base_url: str = ""
    ) -> None:
        super().__init__(page)
        self.base_url = base_url
        self.locators = AccountWishListLocators(page, product_name)

    @property
    def product_row(self) -> Locator:
        return self.locators.product_row

    @property
    def wish_list_items(self) -> Locator:
        return self.locators.remove_item_buttons

    @property
    def empty_wish_list_message(self) -> Locator:
        return self.locators.empty_wish_list_message

    def open(self) -> "WishListPage":
        execute_ui_action(
            self.page,
            "open the wish list page",
            lambda: self.page.goto(
                urljoin(self.base_url, self.WISH_LIST_PATH),
                wait_until="domcontentloaded",
            ),
        )
        return self

    def remove_item(self) -> None:
        execute_ui_action(
            self.page,
            "remove the product from the wish list",
            self.locators.remove_item_button.click,
        )

    def remove_all_items(self) -> None:
        # Bounded by the initial count so a failing removal cannot loop forever.
        for _ in range(self.wish_list_items.count()):
            with self.page.expect_navigation(wait_until="domcontentloaded"):
                execute_ui_action(
                    self.page,
                    "remove an item from the wish list",
                    self.wish_list_items.first.click,
                )
