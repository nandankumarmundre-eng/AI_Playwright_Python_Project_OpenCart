from playwright.sync_api import Locator, Page

from data.web.models import AddressDetails
from pages.base_page import BasePage
from pages.locators.address_book_locators import AddressBookLocators
from utils.playwright_actions import execute_ui_action
from utils.wait_utils import wait_for_element_enabled


class AddressBookPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = AddressBookLocators(page)

    @property
    def heading(self) -> Locator:
        return self.locators.heading

    @property
    def success_message(self) -> Locator:
        return self.locators.success_message

    def address_row(self, address: AddressDetails) -> Locator:
        return self.locators.address_row(address.address_1, address.postcode)

    def edit_address(self) -> "AddressBookPage":
        # A newly registered account has no saved address, so add one instead.
        if self.locators.edit_button().count() == 0:
            execute_ui_action(
                self.page,
                "open the new address form",
                self.locators.new_address_button().click,
            )
            return self
        execute_ui_action(
            self.page,
            "open the first address for editing",
            self.locators.edit_button().click,
        )
        return self

    def update_address(self, address: AddressDetails) -> "AddressBookPage":
        fields = (
            ("first name", self.locators.first_name, address.first_name),
            ("last name", self.locators.last_name, address.last_name),
            ("company", self.locators.company, address.company),
            ("address 1", self.locators.address_1, address.address_1),
            ("address 2", self.locators.address_2, address.address_2),
            ("city", self.locators.city, address.city),
            ("post code", self.locators.postcode, address.postcode),
        )
        for name, locator, value in fields:
            execute_ui_action(
                self.page,
                f"fill in the address {name}",
                lambda locator=locator, value=value: locator.fill(value),
            )
        execute_ui_action(
            self.page,
            "select the address country",
            lambda: self.locators.country.select_option(label=address.country),
        )
        # The site disables the country field while it reloads the regions and
        # drops a disabled field from the submitted form, so wait for the
        # reload to finish before touching the region or submitting.
        execute_ui_action(
            self.page,
            "wait for the region list to reload",
            lambda: wait_for_element_enabled(self.locators.country),
        )
        execute_ui_action(
            self.page,
            "select the address region",
            lambda: self.locators.state.select_option(label=address.state),
        )
        default_radio = (
            self.locators.default_yes
            if address.default_address
            else self.locators.default_no
        )
        execute_ui_action(
            self.page, "choose the default address option", default_radio.check
        )
        execute_ui_action(
            self.page,
            "save the address",
            self.locators.continue_button.click,
        )
        return self
