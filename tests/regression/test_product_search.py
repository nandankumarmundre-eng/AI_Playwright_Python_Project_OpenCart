import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.regression
def test_search_product_displays_matching_product(
    page: Page, base_url: str, storefront_product_name: str
) -> None:
    search_results = HomePage(page, base_url).open().search_for_product(
        storefront_product_name
    )

    expect(search_results.search_heading).to_be_visible()
    expect(search_results.first_product_card).to_be_visible()
    expect(
        search_results.product_heading(storefront_product_name)
    ).to_be_visible()
