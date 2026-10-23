from playwright.sync_api import Locator, Page


class ShoppingCartLocators:
    def __init__(self, page: Page, product_name: str) -> None:
        self.heading: Locator = page.get_by_role(
            "heading", name="Shopping Cart", exact=False
        )
        self.product_row: Locator = page.get_by_role("row").filter(
            has=page.get_by_role("link", name=product_name, exact=True)
        )
