from playwright.sync_api import APIResponse


def assert_status(response: APIResponse, expected_status: int) -> None:
    actual_status = response.status
    if actual_status != expected_status:
        raise AssertionError(
            f"Expected HTTP status {expected_status}, received {actual_status} "
            f"for {response.url}."
        )
