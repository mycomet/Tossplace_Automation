# Android Mobile Test Automation Framework (Appium + Pytest)

Automation framework for Android login testing using Appium and Pytest with Page Object Model architecture.

This project is a mobile test automation framework built using **Appium** and **Pytest** for Android applications.

This project uses the Tossplace app as a test target.

---

# Why This Project

This project was built to design a maintainable and scalable mobile test automation framework for login scenarios using Appium and Pytest.

It focuses on efficiently validating various login cases by:

- Structuring test logic using Page Object Model (POM)
- Separating test data from test implementation
- Handling mobile-specific interruptions such as system popups
- Supporting reusable and data-driven test execution

---

이 프로젝트는 Appium과 Pytest를 활용하여 로그인 시나리오에 대한 유지보수성과 확장성을 고려한 모바일 테스트 자동화 프레임워크를 구축하기 위해 작성되었습니다.

다양한 로그인 케이스를 효율적으로 검증할 수 있도록 다음에 초점을 맞추었습니다:

- Page Object Model(POM)을 적용한 테스트 구조 설계
- 테스트 데이터와 테스트 로직의 분리
- 삼성패스와 같은 시스템 팝업 처리
- 데이터 기반 테스트를 통한 재사용성과 확장성 확보

---

# Features

- Page Object Model (POM) architecture
- Pytest-based test execution
- Test data separation
- Samsung Pass popup handling
- Logging for test execution
- Parameterized test cases

---

# Tech Stack

- Python
- Appium
- Pytest
- Selenium WebDriver
- Android UIAutomator2

---

# Project Structure

```
Tossplace_Automation_V2
│
├── data
│   └── login_data.py
│
├── handlers
│   └── samsung_pass_handler.py
│
├── pages
│   ├── base_page.py
│   └── login_page.py
│
├── tests
│   ├── conftest.py
│   └── test_login.py
│
├── __init__.py
├── config.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Test Strategy

### Page Object Model (POM)

Separates UI logic from test logic for better maintainability.

---

### Test Data Separation

Test data is separated from test logic to improve scalability.

---

### Popup Handling Strategy

Handles Samsung Pass popup to prevent test interruption.

---

### Test Parameterization

Executes test scenarios using pytest parameterization.

```python
@pytest.mark.parametrize("set_name, case", test_params)
```

---

# Test Flow

```
Test Start
   │
   ▼
Launch Application
   │
   ▼
Navigate to Login Screen
   │
   ▼
Select Phone Number Login
   │
   ▼
Handle Samsung Pass Popup (if appears)
   │
   ▼
Enter Login Credentials
   │
   ▼
Click Login Button
   │
   ▼
Handle Samsung Pass Popup (if appears)
   │
   ▼
Test Completed
```

---

# Test Scenarios

- Login attempt without entering credentials
- Login attempt with phone number only (missing password)
- Login attempt with password only (missing phone number)
- Login attempt with valid credentials

---

# Prerequisites

- Python 3.9+
- Appium Server
- Android SDK
- Node.js (for Appium)
- Connected Android device

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Configuration

Edit the following values in `config.py` if needed:

- DEVICE_NAME
- APP_PACKAGE
- APP_ACTIVITY

Example:

```python
options.set_capability("deviceName", "AndroidDevice")
```

---

# CI (GitHub Actions)

This project uses GitHub Actions to automatically validate the test framework on each push and pull request.

The CI pipeline performs:

- Test collection to verify test structure
- Execution of non-device tests (if available)

> Note: Mobile device-based tests require a real Android device and are excluded from CI.  
> These tests are intended to be executed locally.

---

# Run Tests

### Appium Server

The Appium driver is automatically initialized within the test framework.

In most cases, you do not need to manually start the Appium server before running tests.

> Note: Make sure Appium is properly installed and available in your environment.

---

### Run all tests

```bash
pytest -v
```

### Run a specific test file

```bash
pytest tests/test_login.py -v
```

---

# Logging

Test execution logs are printed in the console.

Example:

```
2026-03-12 16:00:21 [INFO] [START] SET1_CASE1 - 로그인 정보 미입력
```