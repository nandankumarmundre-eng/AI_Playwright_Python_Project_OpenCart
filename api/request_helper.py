from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse


from api.endpoints import BOOKING, booking_by_id


def post_json(
    request: APIRequestContext, url: str, payload: dict[str, Any]
) -> APIResponse:
    return request.post(url, data=payload)


def create_booking(
    request: APIRequestContext, payload: dict[str, Any]
) -> APIResponse:
    return post_json(request, BOOKING, payload)


def get_booking(request: APIRequestContext, booking_id: int | str) -> APIResponse:
    return request.get(booking_by_id(booking_id))
