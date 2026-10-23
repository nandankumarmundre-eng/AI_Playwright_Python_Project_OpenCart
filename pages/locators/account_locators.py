from playwright.sync_api import Locator, Page

from constants.messages import ACCOUNT_CREATED_HEADING


class AccountLocators:
    def __init__(self, page: Page) -> None:
        self.created_heading: Locator = page.get_by_role(
            "heading", name=ACCOUNT_CREATED_HEADING, exact=True
        )
