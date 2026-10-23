import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.e2e
@pytest.mark.end_to_end
@pytest.mark.regression
def test_search_add_excel_product_to_cart_and_verify_cart(
    page: Page, base_url: str, storefront_product_name: str
) -> None:
    search_results = HomePage(page, base_url).open().search_for_product(
        storefront_product_name
    )
    expect(search_results.locators.search_heading).to_be_visible()
    expect(
        search_results.locators.product_heading(storefront_product_name)
    ).to_be_visible()
    logger.info(
        "Search results displayed for product %s", storefront_product_name
    )

    product_page = search_results.open_product(storefront_product_name)
    expect(product_page.locators.product_heading).to_be_visible()
    product_page.add_to_cart()
    expect(product_page.locators.add_to_cart_success).to_contain_text(
        "Success: You have added "
        f"{storefront_product_name} to your shopping cart!"
    )

    shopping_cart_page = product_page.open_shopping_cart()
    expect(page).to_have_url(
        f"{base_url.rstrip('/')}/index.php?route=checkout/cart"
    )
    expect(shopping_cart_page.locators.heading).to_be_visible()
    expect(shopping_cart_page.locators.product_row).to_be_visible()
