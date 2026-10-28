import pytest
from playwright.sync_api import Page, expect

from data.web.models import LoginCredentials
from utils.helpers import login_to_account


@pytest.mark.sanity
def test_login_redirects_to_account_page(
    page: Page,
    base_url: str,
    login_credentials: LoginCredentials,
    ) -> None:
    login_page = login_to_account(page, base_url, login_credentials)

    expect(page).to_have_url(
        f"{base_url.rstrip('/')}/index.php?route=account/account"
    )
    expect(login_page.account_heading).to_be_visible()
  