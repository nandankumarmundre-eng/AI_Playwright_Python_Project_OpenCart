from pathlib import Path

from playwright.sync_api import Page


def save_failure_screenshot(page: Page, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(destination), full_page=True)
