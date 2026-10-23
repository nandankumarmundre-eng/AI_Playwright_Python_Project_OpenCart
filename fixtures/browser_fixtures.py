from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, BrowserType, sync_playwright

from config.playwright_config import get_headless_option


@pytest.fixture(scope="session")
def browser(request: pytest.FixtureRequest) -> Generator[Browser, None, None]:
    browser_name = (
        request.config.getoption("--browser")
        or request.config.getini("browser")
        or "chromium"
    )
    if not isinstance(browser_name, str):
        raise pytest.UsageError("--browser must be chromium, firefox, or webkit.")
    headed_option = request.config.getoption("--headed")
    headed = (
        False
        if request.config.getoption("--headless")
        else bool(
            headed_option
            if headed_option is not None
            else request.config.getini("headed")
        )
    )
    with sync_playwright() as playwright:
        browser_types: dict[str, BrowserType] = {
            "chromium": playwright.chromium,
            "firefox": playwright.firefox,
            "webkit": playwright.webkit,
        }
        if headed and browser_name == "chromium":
            browser_instance = browser_types[browser_name].launch(
                headless=False,
                args=["--start-maximized"],
            )
        else:
            browser_instance = browser_types[browser_name].launch(
                headless=get_headless_option(headed)
            )
        yield browser_instance
        browser_instance.close()
