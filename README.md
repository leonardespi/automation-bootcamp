# QA Automation Bootcamp

A modular, hands-on upskilling course that takes functional/manual testers from **zero automation** to **Junior Automation Engineer** level using Python, Selenium, and Page Object Model (POM).

## What you'll learn
- Python fundamentals for testing
- Web automation with Selenium (Chrome headless)
- Page Object Model (POM) architecture
- Assertions, screenshots, and Allure reporting
- CI integration with GitHub Actions
- Debugging & deflaking strategies
- Capstone: design a small, maintainable E2E suite with CI + reports

## Quickstart (GitHub Codespaces)
1. **Open in Codespaces** → This repo includes a `.devcontainer` configured with Python and dev tools.
2. `pip install -r requirements.txt`
3. Run smoke tests: `pytest -q`
4. Generate Allure report locally (optional): `pytest --alluredir=reports/allure`
   - Then `allure serve reports/allure` (requires Allure locally; optional in Codespaces).

## Local Dev (outside Codespaces)
- Python 3.11+ recommended.
- Google Chrome is set up by CI; locally ensure a Chrome or Chromium is installed.
- Tests use `webdriver-manager` to obtain the right ChromeDriver version.

## Repository Map
- `docs/` — theory modules
- `exercises/` — hands-on tasks and starter code
- `tests/` — default CI tests (smoke)
- `pages/` — reusable POM classes
- `reports/` — output folder for generated reports (excluded from VCS except a keep file)

## Contributing (Mentors)
- Open PRs with new exercises or improvements.
- CI runs `pytest` on PRs. Add notes in `docs/` for theory changes.
