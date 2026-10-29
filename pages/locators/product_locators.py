from playwright.sync_api import Locator, Page


class ProductLocators:
    ADD_TO_CART_BUTTON_NAME = "Add to Cart"

    def __init__(self, page: Page, product_name: str) -> None:
        self.product_heading: Locator = page.get_by_role(
            "heading", name=product_name, level=1, exact=True
        )
        self.add_to_cart_button: Locator = page.get_by_role(
            "button", name=self.ADD_TO_CART_BUTTON_NAME, exact=True
        )
        self.add_to_cart_success: Locator = page.locator(".alert-success")
        self.shopping_cart_link: Locator = self.add_to_cart_success.get_by_role(
            "link", name="shopping cart", exact=True
        )
        # Bootstrap tooltips strip the title attribute, leaving the icon-only
        # button without an accessible name, so role/title locators can't match.
        self.add_to_wish_list_button: Locator = page.locator(
            "#content .btn-group button[onclick^='wishlist.add']"
        )
        # The alert has no role/test id; filter by its wish list text so a
        # cart or other success alert can never satisfy the locator.
        self.add_to_wish_list_success: Locator = page.locator(
            ".alert-success"
        ).filter(has_text=f"added {product_name} to your wish list")
        self.wish_list_link: Locator = self.add_to_wish_list_success.get_by_role(
            "link", name="wish list", exact=True
        )
        self.wish_list_product_link: Locator = (
            self.add_to_wish_list_success.get_by_role(
                "link", name=product_name, exact=True
            )
        )

    