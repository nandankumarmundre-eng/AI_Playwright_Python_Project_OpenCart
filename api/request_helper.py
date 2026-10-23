from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse


def post_json(
    request: APIRequestContext, url: str, payload: dict[str, Any]
) -> APIResponse:
    return request.post(url, data=payload)
