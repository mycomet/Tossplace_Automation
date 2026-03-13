import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class LoginPage(BasePage):
    """
    로그인 화면 관련 동작을 담당하는 Page Object.
    화면 진입, 계정 입력, 로그인 수행 및 결과 확인 기능 제공.
    """

    def is_on_login_screen(self):
        try:
            self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("휴대폰 번호 로그인")')
            return True
        except (NoSuchElementException, TimeoutException):
            logging.debug("[CHECK] 로그인 화면 요소 발견 실패")
            return False

    def navigate_to_login_screen(self):
        if self.is_on_login_screen():
            return

        logging.debug("[PAGE] 로그인 화면으로 이동: '프론트 없이 로그인' 클릭")
        self.click(AppiumBy.ANDROID_UIAUTOMATOR, r'new UiSelector().text("프론트 없이 로그인")')

    def select_phone_login(self):
        self.click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("휴대폰 번호 로그인")')

    def enter_login_credentials(self, phone, password):
        inputs = self.find_all(AppiumBy.CLASS_NAME, 'android.widget.EditText')

        if len(inputs) < 2:
            logging.info(f"[PAGE] 로그인 입력 필드 부족 (기대: 2개, 발견: {len(inputs)})")
            raise RuntimeError("로그인 입력 필드를 찾을 수 없음")

        inputs[0].send_keys(phone)
        inputs[1].send_keys(password)
        logging.info("아이디, 비번 입력 완료")

    def click_login_button(self):
        # 로그인 버튼 클릭하기 위해 키보드 닫음
        try:
            self.driver.press_keycode(4)
        except Exception:
            pass

        self.click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("로그인")')

    def get_login_error_message(self):
        """로그인 실패 시 노출되는 에러 메시지 반환."""
        try:
            error = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("ID를 확인해 주세요")')
            return error.text
        except (NoSuchElementException, TimeoutException):
            return None