# TutorialsNinja Playwright/Pytest Framework

A synchronous Playwright/pytest framework organized around Page Objects,
reusable page components, isolated fixtures, environment configuration,
centralized test data, and CI workflows.

## Project layout

- `.github/agents/`, `.github/workflows/`: workspace agents and CI pipelines.
- `config/`: environment selection, browser settings, and `dev.env`, `qa.env`,
  `stage.env`, and `prod.env`.
- `data/web/`, `data/api/`: web workbooks and API test data.
- `pages/`: page objects, reusable `components/`, and `locators/`.
- `fixtures/`: browser, page/context, authentication, environment, and test-data
  fixtures.
- `assertions/`: reusable assertions.
- `tests/`: smoke and end-to-end tests, with regression/sanity directories for
  future suites.
- `utils/`: data readers, browser actions, logging, waits, evidence, and common
  helpers.
- `reports/`: HTML and Allure reports, logs, and failure evidence.
- `api/`, `database/`, `constants/`, and `listeners/`: supporting framework
  modules retained for API/database extensions and shared test behavior.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```powershell
python -m pytest
```

To watch the test in a browser:

```powershell
python -m pytest --headed
```

In headed Chromium runs, the browser starts maximized and uses the available
window size. `pytest.ini` defaults to headed Chromium; the selected environment
file supplies the default URL (`https://tutorialsninja.com/demo/` in `dev.env`).
Tests retry failures once after two seconds, record WebM videos, and retain
screenshots and traces on failure under
`reports/evidence/`. Reports and logs are also stored under `reports/`. On
Windows, video finalization requires the bundled Playwright `ffmpeg` executable
to be allowed by application-control policy. If blocked, tests warn that no
video could be saved. Override defaults from the CLI:

```powershell
python -m pytest --browser firefox --headless --base-url https://example.com/
```

An explicit CLI `--base-url` takes priority, followed by the
`TUTORIALSNINJA_BASE_URL` environment variable, the selected environment file,
and finally the `pytest.ini` fallback. Select marker combinations with pytest's
`-m` expressions, for example:

```powershell
python -m pytest -m "sanity and regression"
python -m pytest -m "sanity and smoke"
```

The supported markers are `smoke`, `e2e`, `regression`, and `sanity`.

The registration test creates a new demo-store account using a unique
Faker-generated name, telephone number, and password with a unique `example.com`
email for each run. After registration succeeds, the details are appended to
`data/web/registered_account_data.xlsx`; this generated workbook is git-ignored.
The login smoke test prefers `TUTORIALSNINJA_LOGIN_EMAIL` and
`TUTORIALSNINJA_LOGIN_PASSWORD` from the environment or a local `.env` file
(which is git-ignored), then falls back to the most recently registered account
in that workbook. For example, add these entries to `.env`:

```dotenv
TUTORIALSNINJA_LOGIN_EMAIL=your-account@example.com
TUTORIALSNINJA_LOGIN_PASSWORD=your-password
```

You can also set both variables in PowerShell before running:

```powershell
$env:TUTORIALSNINJA_LOGIN_EMAIL = "your-account@example.com"
$env:TUTORIALSNINJA_LOGIN_PASSWORD = "your-password"
python -m pytest tests/smoke/test_login.py
```

The product-search smoke test and add-to-cart test read their product from
`data/web/checkout_data.xlsx`, worksheet `products`, using the `product_name`
column through the shared `storefront_product_name` fixture and
`utils/data_reader.py`.

To run against a different compatible environment, set
`TUTORIALSNINJA_BASE_URL` before invoking pytest.

Choose an environment with `TEST_ENV=dev`, `qa`, `stage`, or `prod`.
`TUTORIALSNINJA_BASE_URL` overrides the selected environment file's base URL;
`PLAYWRIGHT_TIMEOUT_MS` overrides its timeout. Update the non-development
environment files before using them against real environments.

To create an HTML report manually, run
`python -m pytest --html=reports/html/pytest_html_report.html --self-contained-html`.
