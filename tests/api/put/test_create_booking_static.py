# Create a booking via the RESTful Booker API using a static request body - Not recommended.
# Data: hard coded inside the test.
# Playwright assertions are for UI elements; API responses use plain pytest assertions.

import pytest
from playwright.sync_api import APIRequestContext

from api.request_helper import create_booking, get_booking
from api.response_validator import assert_status
from utils.api_helper import assert_booking_matches


@pytest.mark.api
def test_create_booking_static(api_request_context: APIRequestContext):
    request_body = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-10-29", "checkout": "2026-10-31"},
        "additionalneeds": "Breakfast",
    }

    response = create_booking(api_request_context, request_body)
    assert_status(response, 200)
    response_body = response.json()
    print(f"Response body: {response_body}")
    assert_booking_matches(response_body["booking"], request_body)

    booking_id = response_body["bookingid"]
    print(f"Booking ID: {booking_id}")

    get_response = get_booking(api_request_context, booking_id)
    assert_status(get_response, 200)
    assert_booking_matches(get_response.json(), request_body)
