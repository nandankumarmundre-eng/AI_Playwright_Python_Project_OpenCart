from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.web.models import LoginCredentials


def login_to_account(
    page: Page, base_url: str, credentials: LoginCredentials
) -> LoginPage:
    login_page = HomePage(page, base_url).open().open_login()
    login_page.login(credentials)
    return login_page
