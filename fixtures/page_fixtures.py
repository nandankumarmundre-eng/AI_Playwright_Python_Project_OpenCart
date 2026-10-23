from collections.abc import Generator
import os
from pathlib import Path
import warnings

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Error as PlaywrightError,
    Page,
)

from config.config import EVIDENCE_DIRECTORY, get_config
from utils.common_utils import safe_filename
from utils.logger import get_logger
from utils.screenshot_utils import save_failure_screenshot

logger = get_logger(__name__)


@pytest.fixture
def browser_context(
    browser: Browser, request: pytest.FixtureRequest
) -> Generator[BrowserContext, None, None]:
    video_dir = EVIDENCE_DIRECTORY / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)
    context = browser.new_context(
        no_viewport=_headed_option(request.config),
        record_video_dir=str(video_dir),
    )
    try:
        yield context
    finally:
        try:
            context.close()
        except PlaywrightError as error:
            if os.name != "nt" or "spawn UNKNOWN" not in str(error):
                raise
            warnings.warn(
                "Playwright could not finalize the WebM video because Windows "
                "blocked its bundled ffmpeg executable.",
                RuntimeWarning,
                stacklevel=2,
            )


@pytest.fixture
def page(
    browser_context: BrowserContext, request: pytest.FixtureRequest
) -> Generator[Page, None, None]:
    page_instance: Page | None = None
    tracing_started = False
    try:
        browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
        tracing_started = True
        page_instance = browser_context.new_page()
        page_instance.set_default_timeout(get_config()["timeout_ms"])
        yield page_instance
    finally:
        report = getattr(request.node, "rep_call", None)
        if report is None or not report.failed:
            report = getattr(request.node, "rep_setup", None)
        failed = report is not None and report.failed
        evidence_dir = EVIDENCE_DIRECTORY
        test_name = safe_filename(request.node.nodeid)

        if failed:
            try:
                screenshot_dir = evidence_dir / "screenshots"
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                if page_instance is not None:
                    save_failure_screenshot(
                        page_instance, screenshot_dir / f"{test_name}.png"
                    )
            except (OSError, PlaywrightError) as error:
                logger.warning(
                    "Could not save failure screenshot for %s: %s",
                    request.node.nodeid,
                    error,
                )

        if tracing_started:
            try:
                if failed:
                    trace_dir = evidence_dir / "traces"
                    trace_dir.mkdir(parents=True, exist_ok=True)
                    browser_context.tracing.stop(
                        path=str(trace_dir / f"{test_name}.zip")
                    )
                else:
                    browser_context.tracing.stop()
            except (OSError, PlaywrightError) as error:
                if not failed:
                    raise
                logger.warning(
                    "Could not save failure trace for %s: %s",
                    request.node.nodeid,
                    error,
                )


def _headed_option(config: pytest.Config) -> bool:
    if config.getoption("--headless"):
        return False
    headed = config.getoption("--headed")
    if headed is not None:
        return headed
    return config.getini("headed")
