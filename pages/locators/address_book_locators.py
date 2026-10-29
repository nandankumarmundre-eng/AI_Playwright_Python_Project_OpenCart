from playwright.sync_api import Locator, Page


class AddressBookLocators:
    def __init__(self, page: Page) -> None:
        self.page = page
        content = page.locator("#content")
        self.heading: Locator = content.get_by_role(
            "heading", name="Address Book Entries", exact=True
        )
        self.address_rows: Locator = content.get_by_role("row")
        self.success_message: Locator = page.locator(".alert-success")

        self.first_name: Locator = page.get_by_label("First Name")
        self.last_name: Locator = page.get_by_label("Last Name")
        self.company: Locator = page.get_by_label("Company")
        self.address_1: Locator = page.get_by_label("Address 1")
        self.address_2: Locator = page.get_by_label("Address 2")
        self.city: Locator = page.get_by_label("City")
        self.postcode: Locator = page.get_by_label("Post Code")
        self.country: Locator = page.get_by_label("Country")
        self.state: Locator = page.get_by_label("Region / State")
        self.default_yes: Locator = page.get_by_role("radio").and_(
            page.locator("input[name='default'][value='1']")
        )
        self.default_no: Locator = page.get_by_role("radio").and_(
            page.locator("input[name='default'][value='0']")
        )
        self.continue_button: Locator = page.get_by_role(
            "button", name="Continue", exact=True
        )

    def edit_button(self) -> Locator:
        return self.address_rows.first.get_by_role(
            "link", name="Edit", exact=True
        )

    def new_address_button(self) -> Locator:
        return self.page.locator("#content").get_by_role(
            "link", name="New Address", exact=True
        )

    def address_row(self, address_1: str, postcode: str) -> Locator:
        return self.address_rows.filter(has_text=address_1).filter(
            has_text=postcode
        )
