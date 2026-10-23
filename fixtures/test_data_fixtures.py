import pytest

from data.web.models import RegistrationDetails, unique_registration_details
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
