# Create a booking via the RESTful Booker API using an external JSON request body - Recommended approach.
# Data: data/api/booking_request.json

import pytest
from playwright.sync_api import APIRequestContext

from api.request_helper import create_booking, get_booking
from api.response_validator import assert_status
from utils.api_helper import assert_booking_matches, load_json_data


@pytest.mark.e2e
def test_create_booking_json(api_request_context: APIRequestContext):
    request_body = load_json_data("booking_request.json")

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
