from dataclasses import dataclass
from uuid import uuid4

from faker import Faker


_FAKER = Faker()


@dataclass(frozen=True)
class LoginCredentials:
    email: str
    password: str


@dataclass(frozen=True)
class RegistrationDetails:
    first_name: str
    last_name: str
    email: str
    telephone: str
    password: str


def unique_registration_details() -> RegistrationDetails:
    unique_id = uuid4().hex
    return RegistrationDetails(
        first_name=_FAKER.first_name(),
        last_name=_FAKER.last_name(),
        email=f"playwright.{unique_id}@example.com",
        telephone=_FAKER.numerify("##########"),
        password=_FAKER.password(
            length=16,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    )
