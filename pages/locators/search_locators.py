from playwright.sync_api import Locator, Page


class HomeSearchLocators:
    def __init__(self, page: Page) -> None:
        self.search_input: Locator = page.get_by_placeholder("Search")
        self.search_button: Locator = page.locator("#search button")


class SearchResultsLocators:
    def __init__(self, page: Page, search_term: str) -> None:
        self.search_heading: Locator = page.get_by_role(
            "heading", name=f"Search - {search_term}", exact=True
        )
        self.product_cards: Locator = page.locator("#content .product-layout")

    def product_heading(self, product_name: str) -> Locator:
        return self.product_cards.get_by_role(
            "heading", name=product_name, exact=True
        )

    def product_link(self, product_name: str) -> Locator:
        return self.product_heading(product_name).get_by_role(
            "link", name=product_name, exact=True
        )
