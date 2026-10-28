from playwright.sync_api import Locator, Page, expect


def wait_for_page_load(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


def wait_for_element_enabled(locator: Locator) -> None:
    expect(locator).to_be_enabled()
