import pytest
from playwright.sync_api import Page, expect

from data.web.models import AddressDetails, LoginCredentials
from pages.my_account_page import MyAccountPage
from utils.helpers import login_to_account

# Automation Workflow
# 1. Navigate to the account page
# 2. Open the address book section
# 3. Click on the Edit button to update the address
# 4. Get the address details from 'address_data.xlsx' in the data/web folder
# 5. Update the address details
# 6. Save the changes
# 7. Verify the success message and updated address details

@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.regression
def test_update_address(
    page: Page,
    address_data: AddressDetails,
    base_url: str,
    login_credentials: LoginCredentials,
) -> None:
    login_to_account(page, base_url, login_credentials)
    address_book = MyAccountPage(page).open_address_book()
    expect(address_book.heading).to_be_visible()

    address_book.edit_address().update_address(address_data)

    expect(address_book.success_message).to_contain_text(
        "Your address has been successfully updated"
    )
    address_row = address_book.address_row(address_data)
    expected_parts = (
        f"{address_data.first_name} {address_data.last_name}",
        address_data.company,
        address_data.address_1,
        address_data.address_2,
        f"{address_data.city} {address_data.postcode}",
        address_data.state,
        address_data.country,
    )
    for part in filter(None, expected_parts):
        expect(address_row).to_contain_text(part)
    print(f'Updated address for: {address_data.first_name} {address_data.last_name}')
    