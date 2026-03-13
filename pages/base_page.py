from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_WAIT

import logging

class BasePage:
    """모든 Page Object의 공통 요소 탐색 및 대기 로직 정의."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_WAIT)

    def find(self, by, value):
        return self.wait.until(lambda d: d.find_element(by, value))

    def click(self, by, value):
        self.find(by, value).click()

    def find_all(self, by, value):
        """
        요소 나타날 때까지 대기 후 리스트 반환.
        미발견 시 빈 리스트 반환.
        """
        try:
            return self.wait.until(lambda d: d.find_elements(by, value) or None)
        except TimeoutException:
            logging.debug(f"[COMMON] 요소 미발견: by={by}, value={value}")
            return []