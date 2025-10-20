import os
from shutil import which
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


def _detect_chrome_binary():
    return (
        os.environ.get("CHROME_BIN")
        or which("chromium")
        or which("chromium-browser")
        or which("google-chrome")
        or which("google-chrome-stable")
    )


@pytest.fixture
def driver():
    user_data_dir = "/tmp/chrome-user-data"
    cache_dir = "/tmp/chrome-cache"
    os.makedirs(user_data_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    chrome_bin = _detect_chrome_binary()
    if not chrome_bin:
        raise RuntimeError(
            "Chrome/Chromium binary not found. Install Chrome/Chromium or set CHROME_BIN."
        )

    options = Options()
    options.binary_location = chrome_bin

    # Minimal, stable flags for containers
    flags = [
        "--headless=new",              # modern headless
        "--no-sandbox",
        "--disable-dev-shm-usage",     # avoid small /dev/shm in containers
        "--window-size=1280,900",      # set size via flag (not via WebDriver call)
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-gpu",               # harmless in headless; keeps consistency
        "--remote-allow-origins=*",    # workaround for some images
        f"--user-data-dir={user_data_dir}",
        f"--disk-cache-dir={cache_dir}",
        "--hide-scrollbars",
    ]
    for f in flags:
        options.add_argument(f)

    # ⚠️ Do NOT use --single-process or --disable-features=VizDisplayCompositor in modern Chrome.
    # ⚠️ Do NOT set a fixed --remote-debugging-port unless you must; defaults are fine.

    drv = webdriver.Chrome(options=options)

    # In headless, Chrome ignores window APIs; rely on --window-size instead.
    # Only attempt set_window_size when *not* headless to avoid session crashes.
    try:
        is_headless = any("--headless" in a for a in options.arguments)
        if not is_headless:
            drv.set_window_size(1280, 900)
    except WebDriverException:
        # Best-effort: if something goes wrong here, continue with the session
        pass

    yield drv
    try:
        drv.quit()
    except Exception:
        pass


def test_login_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # Verify landing page
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "inventory" in driver.current_url
