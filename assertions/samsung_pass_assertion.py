
import logging

def assert_samsung_pass(popup_result, expect_popup, step_label="SPASS"):
    """
    popup_result: handle_samsung_pass() 반환 dict
    - { "found": bool, "closed": bool, "msg": str, "error": str|None }

    expect_popup
    - True → 팝업 떠야 함
    - False → 팝업 없어야 함
    
    step_label: "STEP1", "STEP2" 등 단계 표시용
    """

    found = popup_result["found"]
    closed = popup_result["closed"]
    msg = popup_result["msg"]

    # 로깅은 공통 처리
    logging.info(f"[{step_label}] {msg}")

    # ---- Expect Popup: True ----
    if expect_popup:
        assert found, f"[{step_label}] Expected popup, but none was found"
        assert closed, f"[{step_label}] Popup found but failed to close ({msg})"
        return

    # ---- Expect Popup: False ----
    else:
        assert not found, f"[{step_label}] Popup should NOT appear, but appeared ({msg})"
        return
