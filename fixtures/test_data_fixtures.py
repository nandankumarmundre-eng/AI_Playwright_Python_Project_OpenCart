import pytest

from data.web.models import (
    AddressDetails,
    RegistrationDetails,
    unique_registration_details,
)
from utils.data_reader import DataReaderError, read_excel_data


@pytest.fixture
def registration_details() -> RegistrationDetails:
    return unique_registration_details()


@pytest.fixture
def storefront_product_name() -> str:
    product_data = read_excel_data("checkout_data.xlsx", "products")
    if not product_data or not product_data[0].get("product_name"):
        raise DataReaderError(
            "The first row in 'products' must provide a product_name."
        )
    return product_data[0]["product_name"]

@pytest.fixture
def address_data() -> AddressDetails:
    rows = read_excel_data("address_data.xlsx", "Sheet1")
    if not rows:
        raise DataReaderError("'Sheet1' in address_data.xlsx has no rows.")
    row = rows[0]
    required = (
        "first_name", "last_name", "addr_1", "city", "zip_code",
        "country", "state",
    )
    missing = [column for column in required if not row.get(column)]
    if missing:
        raise DataReaderError(
            f"address_data.xlsx is missing values for: {', '.join(missing)}."
        )
    return AddressDetails(
        first_name=row["first_name"],
        last_name=row["last_name"],
        company=row.get("company", ""),
        address_1=row["addr_1"],
        address_2=row.get("addr_2", ""),
        city=row["city"],
        postcode=row["zip_code"],
        country=row["country"],
        state=row["state"],
        default_address=row.get("Default_addr", "").lower() == "yes",
    )

@pytest.fixture
def wish_list_product_name() -> str:
    product_data = read_excel_data("checkout_data.xlsx", "products")
    if not product_data or not product_data[0].get("wish_list"):
        raise DataReaderError(
            "The first row in 'products' must provide a wish_list."
        )
    return product_data[0]["wish_list"]
