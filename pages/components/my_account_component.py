from playwright.sync_api import Locator, Page

from pages.locators.home_locators import HomeLocators
from pages.login_page import LoginPage
from pages.order_history_page import OrderHistoryPage
from utils.playwright_actions import execute_ui_action


class MyAccountComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = HomeLocators(page)

    @property
    def account_menu(self) -> Locator:
        return self.locators.account_menu

    def open_register(self) -> None:
        execute_ui_action(
            self.page,
            "open the My Account menu",
            self.locators.account_menu.click,
        )
        execute_ui_action(
            self.page,
            "open the registration page",
            self.locators.register_link.click,
        )

    def open_login(self) -> LoginPage:
        execute_ui_action(
            self.page,
            "open the My Account menu",
            self.locators.account_menu.click,
        )
        execute_ui_action(
            self.page,
            "open the login page",
            self.locators.login_link.click,
        )
        return LoginPage(self.page)

    def open_order_history(self) -> OrderHistoryPage:
        execute_ui_action(
            self.page,
            "open the My Account menu",
            self.locators.account_menu.click,
        )
        execute_ui_action(
            self.page,
            "open order history",
            self.locators.order_history_link.click,
        )
        return OrderHistoryPage(self.page)
