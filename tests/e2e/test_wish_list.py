import pytest
from playwright.sync_api import Page, expect

from data.web.models import LoginCredentials
from fixtures.auth_fixtures import login_credentials
from fixtures.test_data_fixtures import wish_list_product_name
from utils.helpers import login_to_account
from pages.home_page import HomePage


# Test scenario
# 1. Enter any existing Product name into the Search text box field - <Refer checkout_data> wish_list<Apple Cinema 30>
# 2. Click on the button having search icon
# 3. Click on the Product displayed in the Search results
# 4. Click on 'Add to Wish List' option on a product that is displayed in the 'Related Products' section of displayed 'Product Display' page (Validate ER-1)
# 5. Click on the 'wish list!' link in the displayed success message (Validate ER-2)"

# expected
# "1. Success message with text -  Success: You have added Apple Cinema 30" to your wish list! should be displayed
# 2. Product should be successfully displayed in the 'My Wish List' page"

@pytest.mark.e2e
@pytest.mark.regression
def test_add_to_wish_list(
    page: Page,
    wish_list_product_name: str,
    base_url: str,
    login_credentials: LoginCredentials,
) -> None:
    product_name = wish_list_product_name
    login_to_account(page, base_url, login_credentials)
    search_results = HomePage(page, base_url).open().search_for_product(
        product_name
    )

    expect(search_results.search_heading).to_be_visible()
    expect(search_results.product_heading(product_name)).to_be_visible()

    product_page = search_results.open_product(product_name)
    product_page.add_to_wish_list()
    expect(product_page.add_to_wish_list_success()).to_be_visible()
    wish_list_page = product_page.open_wish_list()
    expect(wish_list_page.product_row).to_be_visible()
    expect(wish_list_page.empty_wish_list_message).not_to_be_visible()
    wish_list_page.remove_item()
    expect(wish_list_page.empty_wish_list_message).to_be_visible()
    print(f'Product "{product_name}" successfully added to wish list and then removed.')
    
