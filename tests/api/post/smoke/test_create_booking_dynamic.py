# Create a booking via the RESTful Booker API using a dynamic Faker-generated body.
# URLs live in config/urls.py + api/endpoints.py, the request context comes from
# the api_request_context fixture, and calls go through api/request_helper.py.

import pytest
from playwright.sync_api import APIRequestContext

from api.request_helper import create_booking, get_booking
from api.response_validator import assert_status
from utils.api_helper import assert_booking_matches, generate_dynamic_booking_data


@pytest.mark.smoke  
def test_create_booking_dynamic(api_request_context: APIRequestContext):
    request_body = generate_dynamic_booking_data()

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
