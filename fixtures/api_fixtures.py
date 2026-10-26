from collections.abc import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from config.urls import API_BASE_URL


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    yield context
    context.dispose()
