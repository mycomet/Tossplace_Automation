from appium.webdriver.common.appiumby import AppiumBy

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.support.ui import WebDriverWait

def handle_samsung_pass(driver, timeout=2):
    """
    삼성패스 자동완성 팝업이 표시될 경우 닫기 처리.

    팝업이 표시되지 않으면 아무 동작 없음.
    닫기 실패 시 RuntimeError를 발생.

    Args:
        driver: Appium WebDriver 인스턴스
        timeout (int): 팝업 감지 및 닫기 대기 시간(초)
    """

    wait = WebDriverWait(driver, timeout)

    try:
        btn_popup_menu = wait.until(
            lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                r'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/more_act")'
            )
        )
    except TimeoutException:
        return
    
    try:
        btn_popup_menu.click()
        btn_cancel = wait.until(
            lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                r'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/cancel_btn")'
            )
        )
        btn_cancel.click()

    except (
        NoSuchElementException,
        ElementClickInterceptedException,
        TimeoutException
    ) as e:
        raise RuntimeError(
            f"삼성패스 팝업 닫기 실패"
        ) from e