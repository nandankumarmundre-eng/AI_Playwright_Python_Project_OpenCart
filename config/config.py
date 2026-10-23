import os
from typing import TypedDict
from pathlib import Path

from config.environments import DEFAULT_ENVIRONMENT, ENVIRONMENT_FILES
from config.urls import DEFAULT_BASE_URL

CONFIG_DIRECTORY = Path(__file__).resolve().parent
PROJECT_ROOT = CONFIG_DIRECTORY.parent
REPORTS_DIRECTORY = PROJECT_ROOT / "reports"
EVIDENCE_DIRECTORY = REPORTS_DIRECTORY / "evidence"
DEFAULT_TIMEOUT_MS = 10_000


class FrameworkConfig(TypedDict):
    base_url: str
    timeout_ms: int


def _read_environment_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise FileNotFoundError(f"Environment configuration not found: {path}")

    values: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator or not key.strip():
            raise ValueError(
                f"Invalid environment configuration at {path}:{line_number}."
            )
        values[key.strip()] = value.strip().strip("\"'")
    return values


def get_config(default_base_url: str = DEFAULT_BASE_URL) -> FrameworkConfig:
    environment = os.getenv("TEST_ENV", DEFAULT_ENVIRONMENT).strip().lower()
    config_file = ENVIRONMENT_FILES.get(environment)
    if config_file is None:
        supported = ", ".join(sorted(ENVIRONMENT_FILES))
        raise ValueError(
            f"Unsupported TEST_ENV {environment!r}. Choose one of: {supported}."
        )

    file_values = _read_environment_file(CONFIG_DIRECTORY / config_file)
    base_url = os.getenv(
        "TUTORIALSNINJA_BASE_URL",
        file_values.get("BASE_URL", default_base_url),
    ).strip()
    timeout_value = os.getenv(
        "PLAYWRIGHT_TIMEOUT_MS",
        file_values.get("TIMEOUT_MS", str(DEFAULT_TIMEOUT_MS)),
    )

    if not base_url:
        raise ValueError(
            f"Environment configuration {config_file} has no valid BASE_URL."
        )
    try:
        timeout_ms = int(timeout_value)
    except ValueError as error:
        raise ValueError(
            f"Environment configuration {config_file} has an invalid TIMEOUT_MS."
        ) from error
    if timeout_ms <= 0:
        raise ValueError(
            f"Environment configuration {config_file} has an invalid TIMEOUT_MS."
        )

    return {"base_url": base_url, "timeout_ms": timeout_ms}


def get_base_url() -> str:
    return get_config()["base_url"]
