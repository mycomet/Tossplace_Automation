
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class TossplacePage(BasePage):

    # 현재 '로그인 화면'인지 확인
    def on_login_screen(self):
        try:
            self.find(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("휴대폰 번호 로그인")')
            print("현재 로그인 화면입니다.") # 삭제 예정
            return True
        except:
            print("현재 로그인 화면이 아닙니다.")
            return False
        

    def go_to_login_screen(self):
        # 이미 로그인 화면이면 유지
        if self.on_login_screen():
            print("이미 로그인 화면이니 유지합니다.")
            return

        # 로그인 화면 아니면 로그인 버튼이 있는 화면으로 이동
        print("로그인 화면이 아니니 '로그인 하기'버튼을 클릭합니다.")
        self.click(
            AppiumBy.ANDROID_UIAUTOMATOR,
            r'new UiSelector().text("로그인 하기")'
        )
        
    "---로그인 화면 진입 후 필요 기능들---"
    # 휴대폰 번호 로그인' 선택
    def click_phone_login(self):
        btn = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("휴대폰 번호 로그인")')
        btn.click()

    # 휴대폰 번호 및 비밀번호 입력
    def input_info(self, num, pw):
        inputs = self.find_all(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        inputs[0].send_keys(num)
        inputs[1].send_keys(pw)

    # 키패드 제거 위한 여백 클릭
    def empty_space(self):
        btn = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ListView")')
        btn.click()

    # 로그인 버튼 클릭
    def click_login_button(self):
        btn = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("로그인")')
        btn.click()
    
    # ID 틀린 경우 오류 메시지 표출
    def get_error_message(self):
        try:
            error = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("ID를 확인해 주세요")')
            return error.text
        except:
            return None

