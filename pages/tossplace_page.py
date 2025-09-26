# Tossplace 앱 로그인 시도 테스트 위한 기능

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

class TossplacePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    "---앱 첫 화면에서  동작---"
    # '로그인 하기' 진입
    def click_login_entry(self):
        btn = self.wait.until(lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("로그인 하기")'))
        btn.click()


    "---로그인 화면 진입 후 필요 기능들---"
    # 휴대폰 번호 로그인' 선택
    def click_phone_login(self):
        btn = self.wait.until(lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("휴대폰 번호 로그인")'))
        btn.click()

    # 휴대폰 번호 및 비밀번호 입력
    def input_info(self, num, pw):
        inputs = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        inputs[0].send_keys(num)
        inputs[1].send_keys(pw)

    # 키패드가 로그인 버튼을 가려서 찾지 못하니 여백 눌러서 키패드 없앰
    def empty_space(self):
        btn = self.wait.until(lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.ListView")'))
        btn.click()

    # 로그인 버튼 클릭
    def click_login_button(self):
        btn = self.wait.until(lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("로그인")'))
        btn.click()
    
    # ID 틀린 경우 오류 메시지 표출
    def get_error_message(self):
        try:
            error = self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("ID를 확인해 주세요")'))
            return error.text
        except:
            return None
    