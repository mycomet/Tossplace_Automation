
# 단일 세트 (set1)
common_cases = [
    # Case 1: 팝업이 STEP1, STEP2 모두 떠야 함
    {"case": 1, "phone": "", "password": "", "expected_error": None, 
    "samsung_pass": {"STEP1": True, "STEP2": True}},
    
    # Case 2, 3: 팝업이 STEP1은 안 뜨고, STEP2만 떠야 함
    {"case": 2, "phone": "", "password": "", "expected_error": None, 
    "samsung_pass": {"STEP1": False, "STEP2": True}},
    
    {"case": 3, "phone": "", "password": "", "expected_error": None, 
    "samsung_pass": {"STEP1": False, "STEP2": True}},
    
    # Case 4: 팝업이 아예 안 떠야 함 (로그인 실패 케이스)
    {"case": 4, "phone": "01023542476", "password": "qqqaaa", "expected_error": "ID를 확인해 주세요", 
    "samsung_pass": {"STEP1": False, "STEP2": False}},
]

# set 반복 생성
login_case_sets = [
    (f"set{i}", common_cases) for i in range(1, 3)
]

