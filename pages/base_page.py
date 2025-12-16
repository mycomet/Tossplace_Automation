
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.wait.until(
            lambda d: d.find_element(by, value))

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        el = self.find(by, value)
        el.click()
        return el
