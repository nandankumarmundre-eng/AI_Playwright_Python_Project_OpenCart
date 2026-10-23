from playwright.sync_api import Locator, Page


class HomeLocators:
    ACCOUNT_HEADER_SELECTOR = "#top-links"

    def __init__(self, page: Page) -> None:
        self.account_header: Locator = page.locator(self.ACCOUNT_HEADER_SELECTOR)
        self.account_menu: Locator = page.get_by_title("My Account", exact=True)
        self.login_link: Locator = page.get_by_role(
            "link", name="Login", exact=True
        )
        self.register_link: Locator = page.get_by_role(
            "link", name="Register", exact=True
        )
        self.order_history_link: Locator = self.account_header.get_by_role(
            "link", name="Order History", exact=True
        )
