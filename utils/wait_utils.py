from playwright.sync_api import Page


def wait_for_page_load(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")
