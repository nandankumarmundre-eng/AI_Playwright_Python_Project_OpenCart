import pytest
from playwright.sync_api import Page, expect

from constants.messages import WISH_LIST_ADDED_MESSAGE
from pages.home_page import HomePage
from pages.wish_list_page import WishListPage


@pytest.mark.e2e
@pytest.mark.sanity
@pytest.mark.regression
def test_add_to_wish_list(
    page: Page,
    wish_list_product_name: str,
    base_url: str,
    logged_in_with_empty_wish_list: WishListPage,
) -> None:
    """Search for a product, add it to the wish list, and verify it is listed."""
    product_name = wish_list_product_name
    search_results = HomePage(page, base_url).open().search_for_product(
        product_name
    )

    expect(search_results.search_heading).to_be_visible()
    expect(search_results.product_heading(product_name)).to_be_visible()

    product_page = search_results.open_product(product_name)
    product_page.add_to_wish_list()
    expect(product_page.add_to_wish_list_success()).to_contain_text(
        WISH_LIST_ADDED_MESSAGE.format(product_name=product_name)
    )
    expect(product_page.wish_list_product_link()).to_be_visible()
    expect(product_page.wish_list_link()).to_be_visible()
    wish_list_page = product_page.open_wish_list()
    expect(wish_list_page.product_row).to_be_visible()
    expect(wish_list_page.wish_list_items).to_have_count(1)
    expect(wish_list_page.empty_wish_list_message).not_to_be_visible()
