from playwright.sync_api import Locator, Page

class AccountWishListLocators:
    EMPTY_WISH_LIST_TEXT = "Your wish list is empty."

    def __init__(self, page: Page, product_name: str) -> None:
        self.page = page
        self.product_row: Locator = page.get_by_role("row").filter(
            has=page.get_by_role("link", name=product_name, exact=True)
        )
        self.empty_wish_list_message: Locator = page.get_by_text(
            self.EMPTY_WISH_LIST_TEXT, exact=True
        )
        # Icon-only link: the tooltip script strips its title, so match the href.
        self.remove_item_button: Locator = self.product_row.locator(
            "a[href*='account/wishlist&remove=']"
        )
