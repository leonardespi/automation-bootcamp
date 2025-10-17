from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator, text: str, clear: bool = True):
        el = self.wait.until(lambda d: d.find_element(*locator))
        if clear:
            el.clear()
        el.send_keys(text)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
