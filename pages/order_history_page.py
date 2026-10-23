from playwright.sync_api import Page

from pages.locators.order_history_locators import OrderHistoryLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = OrderHistoryLocators(page)
