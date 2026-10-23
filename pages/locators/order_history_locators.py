from playwright.sync_api import Locator, Page

from constants.messages import ORDER_HISTORY_HEADING


class OrderHistoryLocators:
    def __init__(self, page: Page) -> None:
        self.heading: Locator = page.get_by_role(
            "heading", name=ORDER_HISTORY_HEADING, exact=True
        )
