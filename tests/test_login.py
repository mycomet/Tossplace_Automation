# 로그인 테스트 케이스
# 다양한 입력 조건을 파라미터화하여 검증

import pytest
from pages.tossplace_page import TossplacePage
from utils.spass_handler import handle_Spass

def login_flow(driver, phone, password, case):
    page = TossplacePage(driver)

    # 로그인 화면 진입 전 케이스
    if case == 1:
        page.click_login_entry()
        page.click_phone_login()
        handle_Spass(driver)
        page.empty_space()
        page.input_info(phone, password)

    # 로그인 화면 진입 후 케이스
    else:
        page.click_phone_login()
        page.input_info(phone, password)

    page.click_login_button()
    handle_Spass(driver)
    print(f"TC{case} 완료")
    return page


@pytest.mark.parametrize("phone,password,expected_error,step", [
    ("", "", None, 1),             # 케이스1: 미입력
    ("01011112222", "", None, 2),    # 케이스2: 비번 없음
    ("", "1234", None, 3),           # 케이스3: 번호 없음
    ("01023542476", "qqqaaa", "ID를 확인해 주세요", 4)  # 케이스4: 잘못된 ID/PW
])

def test_login(driver, phone, password, expected_error, step):
    page = login_flow(driver, phone, password, step)

    actual_error = page.get_error_message()

    if expected_error:
        assert actual_error == expected_error
    else:
        assert actual_error is None


