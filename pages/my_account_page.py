from playwright.sync_api import Locator, Page

from pages.address_book_page import AddressBookPage
from pages.base_page import BasePage
from pages.locators.my_account_locators import MyAccountLocators
from pages.order_history_page import OrderHistoryPage
from utils.playwright_actions import execute_ui_action


class MyAccountPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = MyAccountLocators(page)

    @property
    def heading(self) -> Locator:
        return self.locators.heading

    @property
    def my_orders_heading(self) -> Locator:
        return self.locators.my_orders_heading

    @property
    def affiliate_heading(self) -> Locator:
        return self.locators.affiliate_heading

    @property
    def newsletter_heading(self) -> Locator:
        return self.locators.newsletter_heading

    @property
    def sidebar_links(self) -> Locator:
        return self.locators.sidebar_links

    @property
    def logout_link(self) -> Locator:
        return self.locators.sidebar_logout_link

    def open_edit_account(self) -> None:
        execute_ui_action(
            self.page,
            "open the edit account page",
            self.locators.edit_account_link.click,
        )

    def open_change_password(self) -> None:
        execute_ui_action(
            self.page,
            "open the change password page",
            self.locators.change_password_link.click,
        )

    def open_address_book(self) -> AddressBookPage:
        execute_ui_action(
            self.page,
            "open the address book",
            self.locators.address_book_link.click,
        )
        return AddressBookPage(self.page)

    def open_wish_list(self) -> None:
        execute_ui_action(
            self.page,
            "open the wish list from My Account",
            self.locators.wish_list_link.click,
        )

    def open_order_history(self) -> OrderHistoryPage:
        execute_ui_action(
            self.page,
            "open order history from My Account",
            self.locators.order_history_link.click,
        )
        return OrderHistoryPage(self.page)

    def logout(self) -> None:
        execute_ui_action(
            self.page,
            "log out from My Account",
            self.locators.sidebar_logout_link.click,
        )
