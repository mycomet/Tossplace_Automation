
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait

def handle_samsung_pass(driver, quick_timeout=1, action_timeout=3):
    """
    삼성패스 팝업을 찾고(있다면) 닫기를 시도.
    검증(expect) 로직은 포함하지 않음 — 단순 동작만 수행하고 상태 리턴.
    
    Returns dict:
        {
            "found": bool,      # 팝업을 찾았는가
            "closed": bool,     # 닫기 시도가 성공했는가 (팝업이 없으면 True로 간주하지 않음; 아래 참조)
            "error": str|None,  # 예외 타입 문자열 (있다면)
            "msg": str          # 설명용 메시지
        }
    """

    # 팝업 존재 여부 확인 대기 시간 (1초만 기다리고 없으면 바로 통과)
    quick_wait = WebDriverWait(driver, quick_timeout) 
    # 팝업이 뜬 후, 취소 버튼이 나타날 때까지 기다리는 시간
    action_wait = WebDriverWait(driver, action_timeout)

    # 1) 팝업 요소(메뉴 버튼) 탐색
    try:
        view_btn = quick_wait.until(
            lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                r'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/more_act")'
            )
        )
        popup_found = True

    except TimeoutException:
        # 팝업이 없음
        return {
            "found": False, 
            "closed": False, 
            "error": None, 
            "msg": "Popup not shown"
            }

    # 2) 팝업을 찾았으니 닫기 시도
    try:
        view_btn.click()

        cancel_btn = action_wait.until(
            lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                r'new UiSelector().resourceId("com.samsung.android.samsungpassautofill:id/cancel_btn")'
            )
        )
        cancel_btn.click()

        return {
            "found": True, 
            "closed": True, 
            "error": None, 
            "msg": "Popup found and closed"
            }

    except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as e:
        # 팝업은 있었지만 닫기 중 에러 발생 (버튼 없음, 클릭 실패 등)
        return {
            "found": True,
            "closed": False,
            "error": type(e).__name__,
            "msg": f"Popup found but closing failed: {type(e).__name__}"
        }
    except Exception as e:
        # 기타 예외
        return {
            "found": True,
            "closed": False,
            "error": type(e).__name__,
            "msg": f"Popup found but unexpected error: {type(e).__name__}"
        }

