from playwright.sync_api import Locator, Page

from constants.messages import REGISTER_ACCOUNT_HEADING


class RegisterLocators:
    FIRST_NAME_PLACEHOLDER = "First Name"
    LAST_NAME_PLACEHOLDER = "Last Name"
    EMAIL_PLACEHOLDER = "E-Mail"
    TELEPHONE_PLACEHOLDER = "Telephone"
    PASSWORD_PLACEHOLDER = "Password"
    CONFIRM_PASSWORD_PLACEHOLDER = "Password Confirm"

    def __init__(self, page: Page) -> None:
        self.heading: Locator = page.get_by_role(
            "heading", name=REGISTER_ACCOUNT_HEADING, exact=True
        )
        self.first_name: Locator = page.get_by_placeholder(
            self.FIRST_NAME_PLACEHOLDER, exact=True
        )
        self.last_name: Locator = page.get_by_placeholder(
            self.LAST_NAME_PLACEHOLDER, exact=True
        )
        self.email: Locator = page.get_by_placeholder(
            self.EMAIL_PLACEHOLDER, exact=True
        )
        self.telephone: Locator = page.get_by_placeholder(
            self.TELEPHONE_PLACEHOLDER, exact=True
        )
        self.password: Locator = page.get_by_placeholder(
            self.PASSWORD_PLACEHOLDER, exact=True
        )
        self.confirm_password: Locator = page.get_by_placeholder(
            self.CONFIRM_PASSWORD_PLACEHOLDER, exact=True
        )
        self.newsletter_no: Locator = page.get_by_role("radio", name="No", exact=True)
        self.privacy_policy_checkbox: Locator = page.get_by_role("checkbox")
        self.continue_button: Locator = page.get_by_role(
            "button", name="Continue", exact=True
        )
