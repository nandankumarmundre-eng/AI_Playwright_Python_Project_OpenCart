import pytest

from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_runtest_logstart(nodeid: str, location: tuple[str, int | None, str]) -> None:
    logger.info("Starting test %s", nodeid)


def pytest_runtest_logfinish(
    nodeid: str, location: tuple[str, int | None, str]
) -> None:
    logger.info("Finished test %s", nodeid)
