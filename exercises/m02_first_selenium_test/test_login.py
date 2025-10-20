import os
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def get_chrome_binary():
    possible_paths = [
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        os.getenv("CHROME_BIN"),
    ]
    
    for path in possible_paths:
        if path and Path(path).exists():
            return path
    
    return None


def create_chrome_options():
    options = Options()
    
    chrome_binary = get_chrome_binary()
    if chrome_binary:
        options.binary_location = chrome_binary
    
    #Comment the line below to see the browser window
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-allow-origins=*")
    
    return options


@pytest.fixture
def driver():
    temp_dir = Path("/tmp/chrome-test-profile")
    
    if temp_dir.exists():
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    options = create_chrome_options()
    options.add_argument(f"--user-data-dir={temp_dir}")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.mark.smoke
def test_login_demosite(driver):
    driver.get("https://www.leonardespi.me/automation-demo-site/")
    
    wait = WebDriverWait(driver, 10)
    
    username_field = wait.until(
        EC.presence_of_element_located((By.ID, "input-text"))
    )
    username_field.send_keys("standard_user")
    
    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("automation is so cool")
    
    email = driver.find_element(By.ID, "input-email")
    email.send_keys("standard_user@example.com")
    
    assert username_field.get_attribute("value") == "standard_user"
    assert password_field.get_attribute("value") == "automation is so cool"
    assert email.get_attribute("value") == "standard_user@example.com"