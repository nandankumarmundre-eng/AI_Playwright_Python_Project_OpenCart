from collections.abc import Callable
from typing import TypeVar

from playwright.sync_api import Error as PlaywrightError, Page

_Result = TypeVar("_Result")


class UIActionError(RuntimeError):
    """A UI action failure enriched with the current page and operation."""


def execute_ui_action(
    page: Page, action_description: str, action: Callable[[], _Result]
) -> _Result:
    try:
        result = action()
    except PlaywrightError as error:
        raise UIActionError(
            f"Failed to {action_description} at {page.url or '<unknown URL>'}."
        ) from error
    else:
        return result
