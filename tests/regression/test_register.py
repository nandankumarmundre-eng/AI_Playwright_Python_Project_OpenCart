import pytest
from playwright.sync_api import Page, expect

from data.web.models import RegistrationDetails
from pages.home_page import HomePage
from utils.registered_account_data import save_registered_account


@pytest.mark.e2e
@pytest.mark.end_to_end
@pytest.mark.regression
def test_register_new_account_from_my_account_header(
    page: Page, base_url: str, registration_details: RegistrationDetails
) -> None:
    register_page = HomePage(page, base_url).open().open_registration()
    expect(register_page.locators.heading).to_be_visible()

    success_page = register_page.submit_registration(registration_details)
    expect(success_page.locators.created_heading).to_be_visible()
    save_registered_account(registration_details)
