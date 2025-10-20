import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from exercises.03-page-object-model.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_size(1280, 900)
    yield driver
    driver.quit()

def test_login_with_pom(driver):
    page = LoginPage(driver).open().login_as("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "inventory" in driver.current_url
