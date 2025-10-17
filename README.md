# QA Automation Bootcamp

A modular, hands-on upskilling course that takes functional/manual testers from **zero automation** to **Junior Automation Engineer** level using Python, Selenium, and Page Object Model (POM).

You might also wanna check the demo website you'll use for testing: [here](http://www.leonardespi.me/automation-testers-handbook-demo/)

## What you'll learn
- Python fundamentals for testing
- Web automation with Selenium (Chrome headless)
- Page Object Model (POM) architecture
- Assertions, screenshots, and Allure reporting
- CI integration with GitHub Actions
- Debugging & deflaking strategies
- Capstone: design a small, maintainable E2E suite with CI + reports

## Quickstart (GitHub Codespaces)
1. First of all, fork this repo into your gh account with this link: [fork me](https://github.com/leonardespi/qa-automation-bootcamp/fork)
2. **Open the course guide here** → [Open me](https://www.leonardespi.me/qa-automation-bootcamp/)
3. Follow the course!!

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
