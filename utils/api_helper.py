import json
from datetime import timedelta
from pathlib import Path
from typing import Any

from faker import Faker

fake = Faker()

API_DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data" / "api"


def load_json_data(file_name: str) -> dict[str, Any]:
    with (API_DATA_DIRECTORY / file_name).open(encoding="utf-8") as file:
        return json.load(file)


def assert_booking_matches(actual: dict[str, Any], expected: dict[str, Any]) -> None:
    assert actual == expected, f"Booking mismatch: expected {expected}, got {actual}"


def generate_dynamic_booking_data() -> dict[str, Any]:
    checkin = fake.date_between(start_date="+1d", end_date="+30d")
    checkout = checkin + timedelta(days=fake.random_int(min=1, max=10))
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=1000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": checkin.strftime("%Y-%m-%d"),
            "checkout": checkout.strftime("%Y-%m-%d"),
        },
        "additionalneeds": fake.random_element(
            ["Breakfast", "Lunch", "Dinner", "Late checkout", "Parking"]
        ),
    }
