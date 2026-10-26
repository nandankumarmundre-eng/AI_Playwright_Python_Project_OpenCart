ACCOUNT_REGISTER = "index.php?route=account/register"
ACCOUNT_LOGIN = "index.php?route=account/login"

# Restful Booker API (relative to config.urls.API_BASE_URL)
BOOKING = "booking"


def booking_by_id(booking_id: int | str) -> str:
    return f"{BOOKING}/{booking_id}"
