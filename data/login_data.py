"""
로그인 테스트 시나리오 데이터 세트.

- expected_error: 에러 미발생 시 None 설정.
"""

# 공통 로그인 테스트 케이스
common_cases = [
    {
        "case_id": 1,
        "description": "로그인 정보 미입력",
        "phone": "",
        "password": "",
        "expected_error": None,
    },
    {
        "case_id": 2,
        "description": "비밀번호 미입력",
        "phone": "01011112222",
        "password": "",
        "expected_error": None,
    },
    {
        "case_id": 3,
        "description": "휴대폰 번호 미입력",
        "phone": "",
        "password": "1234",
        "expected_error": None,
    },
    {
        "case_id": 4,
        "description": "잘못된 계정 정보 입력",
        "phone": "01023542476",
        "password": "qqqaaa",
        "expected_error": "ID를 확인해 주세요",
    },
]

# 테스트 반복 생성 위한 세트 구성
login_case_sets = [
    (f"set{i}", common_cases) for i in range(1, 3)
]