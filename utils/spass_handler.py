# 갤럭시 사용자 삼성패스 로그인 팝업 발생 시 취소 처리 위함

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def handle_Spass(driver):
    wait = WebDriverWait(driver, 5)

    try:
        view = wait.until(lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/more_act")'
        ))
    except TimeoutException:
        print("\n삼성패스 팝업 없음")
        return

    if view.is_displayed():
        view.click()
        try:
            cancel = wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/cancel_btn")'
            ))
        except TimeoutException:
            print("취소 버튼 탐색 실패")
            return

        if cancel.is_displayed():
            cancel.click()
            print("\n삼성패스 취소 완료")
