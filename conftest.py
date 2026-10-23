import pytest

pytest_plugins = (
    "listeners.test_listener",
    "fixtures.browser_fixtures",
    "fixtures.page_fixtures",
    "fixtures.auth_fixtures",
    "fixtures.environment_fixtures",
    "fixtures.test_data_fixtures",
)

from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_configure(config: pytest.Config) -> None:
    for directory in (
        config.rootpath / "reports/html",
        config.rootpath / "reports/allure-results",
        config.rootpath / "reports/allure-report",
        config.rootpath / "reports/logs",
        config.rootpath / "reports/evidence/screenshots",
        config.rootpath / "reports/evidence/videos",
        config.rootpath / "reports/evidence/traces",
    ):
        directory.mkdir(parents=True, exist_ok=True)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addini(
        "base_url",
        "Default storefront URL used when --base-url is not supplied.",
        type="string",
    )
    parser.addini(
        "browser",
        "Default browser engine used when --browser is not supplied.",
        type="string",
    )
    parser.addini(
        "headed",
        "Whether to launch a visible browser by default.",
        type="bool",
    )
    parser.addoption(
        "--browser",
        action="store",
        choices=("chromium", "firefox", "webkit"),
        default=None,
        help="Browser engine to launch (overrides pytest.ini).",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=None,
        help="Run the browser with a visible window (overrides pytest.ini).",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run headless even if pytest.ini or addopts enables --headed.",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Storefront URL (overrides pytest.ini and environment settings).",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[None]
):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
    if report.when == "call":
        if report.failed and call.excinfo is not None:
            logger.error("Test %s failed: %s", item.nodeid, call.excinfo.value)
        logger.info("Test %s %s", item.nodeid, report.outcome)
