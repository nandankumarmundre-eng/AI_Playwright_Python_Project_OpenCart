"""Centralized Playwright launch settings."""


def get_headless_option(headed: bool) -> bool:
    return not headed
