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
