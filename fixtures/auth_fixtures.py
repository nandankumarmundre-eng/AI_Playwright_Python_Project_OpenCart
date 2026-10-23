import os
from pathlib import Path

import pytest

from data.web.models import LoginCredentials
from utils.registered_account_data import read_latest_login_credentials


@pytest.fixture
def login_credentials() -> LoginCredentials:
    env_file = Path(__file__).resolve().parents[1] / ".env"
    file_values: dict[str, str] = {}
    if env_file.is_file():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            key, separator, value = line.partition("=")
            if separator and key.strip() in {
                "TUTORIALSNINJA_LOGIN_EMAIL",
                "TUTORIALSNINJA_LOGIN_PASSWORD",
            }:
                file_values[key.strip()] = value.strip().strip("\"'")

    email = os.getenv(
        "TUTORIALSNINJA_LOGIN_EMAIL",
        file_values.get("TUTORIALSNINJA_LOGIN_EMAIL"),
    )
    password = os.getenv(
        "TUTORIALSNINJA_LOGIN_PASSWORD",
        file_values.get("TUTORIALSNINJA_LOGIN_PASSWORD"),
    )
    if email and password:
        return LoginCredentials(email=email, password=password)

    try:
        return read_latest_login_credentials()
    except (OSError, ValueError) as error:
        raise pytest.UsageError(
            "Set TUTORIALSNINJA_LOGIN_EMAIL and "
            "TUTORIALSNINJA_LOGIN_PASSWORD, or run the registration test to "
            "create login data in data/web/registered_account_data.xlsx."
        ) from error
