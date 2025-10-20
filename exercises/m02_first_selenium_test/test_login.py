import os
from shutil import which
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    # Writable profile/cache in containers
    user_data_dir = "/tmp/chrome-user-data"
    cache_dir = "/tmp/chrome-cache"
    os.makedirs(user_data_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    chrome_bin = _detect_chrome_binary()
    if not chrome_bin:
        raise RuntimeError("Chrome/Chromium binary not found. Install chromium and/or set CHROME_BIN.")

    # Build flags explicitly (don’t try to mutate options.arguments)
    flags = [
        "--headless",                      # use legacy headless for container stability
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-features=VizDisplayCompositor",
        "--remote-allow-origins=*",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,900",
        f"--user-data-dir={user_data_dir}",
        f"--disk-cache-dir={cache_dir}",
        "--remote-debugging-port=9222",    # fixed port helps avoid DevToolsActivePort issue
        "--single-process",                # helps on some base images
    ]

    options = Options()
    options.binary_location = chrome_bin
    for f in flags:
        options.add_argument(f)

    # Selenium Manager will resolve the matching driver
    drv = webdriver.Chrome(options=options)
    drv.set_window_size(1280, 900)
    yield drv
    drv.quit()

def test_login_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # Verify landing page
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "inventory" in driver.current_url
