from playwright.sync_api import Page

from data.web.models import RegistrationDetails
from pages.locators.register_locators import RegisterLocators
from pages.base_page import BasePage
from pages.registration_success_page import RegistrationSuccessPage
from utils.playwright_actions import execute_ui_action


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = RegisterLocators(page)

    def submit_registration(
        self, details: RegistrationDetails
    ) -> RegistrationSuccessPage:
        execute_ui_action(
            self.page,
            "fill in the registration form",
            lambda: self._fill_and_submit(details),
        )
        return RegistrationSuccessPage(self.page)

    def _fill_and_submit(self, details: RegistrationDetails) -> None:
        self.locators.first_name.fill(details.first_name)
        self.locators.last_name.fill(details.last_name)
        self.locators.email.fill(details.email)
        self.locators.telephone.fill(details.telephone)
        self.locators.password.fill(details.password)
        self.locators.confirm_password.fill(details.password)
        self.locators.newsletter_no.check()
        self.locators.privacy_policy_checkbox.check()
        self.locators.continue_button.click()
