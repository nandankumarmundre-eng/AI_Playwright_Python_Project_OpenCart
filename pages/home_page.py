from playwright.sync_api import Page

from pages.components.home_search_component import HomeSearchComponent
from pages.components.my_account_component import MyAccountComponent
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_results_page import SearchResultsPage
from utils.playwright_actions import execute_ui_action


class HomePage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page)
        self.base_url = base_url
        self.my_account = MyAccountComponent(page)
        self.search = HomeSearchComponent(page)

    def open(self) -> "HomePage":
        execute_ui_action(
            self.page,
            "open the storefront home page",
            lambda: self.page.goto(
                self.base_url, wait_until="domcontentloaded"
            ),
        )
        return self

    def open_registration(self) -> RegistrationPage:
        self.my_account.open_register()
        return RegistrationPage(self.page)

    def open_login(self) -> LoginPage:
        return self.my_account.open_login()

    def search_for_product(self, search_term: str) -> SearchResultsPage:
        self.search.search(search_term)
        return SearchResultsPage(self.page, search_term)
