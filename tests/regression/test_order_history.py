import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from data.web.models import LoginCredentials
from utils.helpers import login_to_account



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity 
def test_order_history_opens_from_header_after_login(
    page: Page,
    base_url: str,
    login_credentials: LoginCredentials,
) -> None:
    login_page = login_to_account(page, base_url, login_credentials)

    expect(page).to_have_url(
        f"{base_url.rstrip('/')}/index.php?route=account/account"
    )
    expect(login_page.account_heading).to_be_visible()

    order_history_page = HomePage(page, base_url).my_account.open_order_history()
    expect(page).to_have_url(
        f"{base_url.rstrip('/')}/index.php?route=account/order"
    )
    expect(order_history_page.heading).to_be_visible()
