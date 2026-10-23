import pytest

from config.config import get_config
from config.urls import DEFAULT_BASE_URL


@pytest.fixture
def base_url(request: pytest.FixtureRequest) -> str:
    cli_base_url = request.config.getoption("--base-url")
    invocation_args = request.config.invocation_params.args
    if cli_base_url and any(
        argument == "--base-url" or argument.startswith("--base-url=")
        for argument in invocation_args
    ):
        return cli_base_url

    ini_base_url = request.config.getini("base_url")
    return get_config(ini_base_url or DEFAULT_BASE_URL)["base_url"]
