
import copy
import pytest
import time
import logging, sys
from pages.login_page import TossplacePage
from handlers.samsung_pass_handler import handle_samsung_pass
from data.login_data import login_case_sets
from assertions.samsung_pass_assertion import assert_samsung_pass


# ✅ pytest parametrize용 데이터 생성
test_params = [
    (set_name, copy.deepcopy(case))
    for set_name, cases in login_case_sets
    for case in cases
]

def login_flow(driver, phone, password, case):
    page = TossplacePage(driver)

    DEFAULT_POPUP_RESULT = {
            "found": False, 
            "closed": True, # 해당 단계에서 무언가 닫았을 필요는 없으므로 True로 두는 것이 일반적
            "msg": "Popup processing skipped or not applicable."
            }

    popup1 = DEFAULT_POPUP_RESULT.copy()
    popup2 = DEFAULT_POPUP_RESULT.copy()

    if case['case'] == 1:
        page.click_phone_login()
        popup1 = handle_samsung_pass(driver)
        page.empty_space()
        page.input_info(phone, password)

    else:
        page.click_phone_login()
        page.input_info(phone, password)

    page.click_login_button()
    popup2 = handle_samsung_pass(driver)

    return {
        "page": page,
        "first_popup": popup1,
        "second_popup": popup2
    }

def id_func(param):
    # pytest가 tuple로 넘길 수도, 각각의 값으로 넘길 수도 있어서 안전하게 처리
    try:
        # param이 튜플이고, 두 번째가 딕셔너리면
        if isinstance(param, tuple) and len(param) >= 2 and isinstance(param[1], dict):
            return f"{param[0]}_case{param[1]['case']}"
        # param이 그냥 dict일 수도 있음
        elif isinstance(param, dict) and 'case' in param:
            return f"case{param['case']}"
        # 그냥 문자열이나 숫자면 그대로 반환
        return str(param)
    except Exception:
        return str(param)


@pytest.mark.parametrize("set_name, case", test_params, ids=id_func)

def test_login(driver, page, request, ensure_login_screen, set_name, case):

    phone = case["phone"]
    password = case["password"]
    expected_error = case["expected_error"]
    samsung_pass = case["samsung_pass"]

    case_id = f"{set_name.upper()}_CASE{case['case']}"
    # [CASE] 케이스 시작
    logging.info(f"[CASE] [{case_id}] starting")
    logging.info(f"[INFO] Login Info → Phone = {phone}, Password = {password}")

    run_results = login_flow(driver, phone, password, case)

    popup1 = run_results["first_popup"]
    popup2 = run_results["second_popup"]

    assert_samsung_pass(popup1, samsung_pass["STEP1"], "STEP1")

    time.sleep(1)

    assert_samsung_pass(popup2, samsung_pass["STEP2"], "STEP2")

    page_object = run_results["page"]
    actual_error = page_object.get_error_message()

    if actual_error is not None:
        actual_error = actual_error.strip() or None
        logging.info(f"{actual_error}")
    assert actual_error == expected_error

    # [PASS] 케이스 완료
    logging.info(f"[PASS][{set_name.upper()}_CASE{case['case']}] complete")

