import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.e2e
def test_storefront_home_page_loads(page: Page, base_url: str) -> None:
    home_page = HomePage(page, base_url).open()

    expect(page).to_have_title("Your Store")
    expect(home_page.my_account.account_menu).to_be_visible()
