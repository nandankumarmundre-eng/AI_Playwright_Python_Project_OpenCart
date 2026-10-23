from typing import TypedDict


class RegistrationPayload(TypedDict):
    firstname: str
    lastname: str
    email: str
    telephone: str
    password: str
    confirm: str
    agree: str
