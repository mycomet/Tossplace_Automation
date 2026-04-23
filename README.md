# Android Mobile Test Automation Framework (Appium + Pytest)

[![CI Status](https://github.com/mycomet/android-test-automation-framework/actions/workflows/test.yml/badge.svg)](https://github.com/mycomet/android-test-automation-framework/actions)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Android-green)
![Framework](https://img.shields.io/badge/Appium-Automation-orange)
![Test](https://img.shields.io/badge/Pytest-Framework-yellow)
![Report](https://img.shields.io/badge/Allure-Report-purple)

An automation framework for Android login testing built with Appium and Pytest,
using the Page Object Model architecture.

This project is a **mobile test automation framework** designed to validate login scenarios
of the Tossplace app, with a focus on **scalability, maintainability, and CI integration**.

---

## 🚀 Test Reports

- 🧪 CI Report → https://mycomet.github.io/android-test-automation-framework/ci/

- 📱 Mobile Report → https://mycomet.github.io/android-test-automation-framework/mobile/

> Automated mobile testing with CI integration and Allure reporting

---

## 🧠 Why This Project

Mobile login testing often requires repeatedly validating multiple input scenarios
(e.g., missing inputs, partial inputs, invalid credentials),
which can be time-consuming and inefficient when done manually.

This project was created to automate and streamline the validation of these common login cases,
improving testing speed and consistency.

The framework focuses on:

* Automating repetitive login scenarios
* Structuring test logic using Page Object Model (POM)
* Handling mobile-specific interruptions such as Samsung Pass popup
* Enabling continuous validation through CI and automated reporting

Additionally, the framework is designed to be maintainable,
so that UI changes can be handled by updating the Page Object layer
without restructuring the entire test suite.

---

이 프로젝트는 반복적으로 수행되는 로그인 테스트를
보다 빠르고 일관성 있게 검증하기 위해 작성되었습니다.

특히 다양한 로그인 입력 케이스(미입력, 부분 입력, 잘못된 입력 등)를
자동화하여 테스트 효율을 높이는 데 목적이 있습니다.

또한 다음과 같은 설계에 초점을 맞추었습니다:

* 반복적인 로그인 시나리오 자동화
* Page Object Model(POM)을 통한 테스트 구조 분리
* 삼성패스와 같은 모바일 환경 특이 요소 처리
* CI 및 자동 리포트를 통한 지속적인 검증

더불어, UI 변경이 발생하더라도
Page Object 레이어만 수정하여 테스트를 유지할 수 있도록 설계되었습니다.

---

## ⚠️ Note

This project was originally implemented based on a previous version of the Tossplace app.

The current version of the app has introduced changes to the login flow,
so some test scenarios may no longer work as originally implemented.

However, the framework is designed with maintainability in mind,
allowing the test logic to be updated by modifying the Page Object layer
without changing the overall structure.

---

## 🚀 Key Features

* Page Object Model (POM) architecture
* Pytest-based test execution
* Test data separation
* Samsung Pass popup handling
* Logging for test execution
* Parameterized test cases
* CI pipeline with GitHub Actions
* Allure test reporting with GitHub Pages deployment

---

## 🧩 Tech Stack

* Python
* Appium
* Pytest
* Selenium WebDriver
* Android UIAutomator2
* GitHub Actions
* Allure Report

---

## 📁 Project Structure

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
│   ├── test_login.py
│   └── test_smoke.py   # CI validation tests
│
├── config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Test Strategy

### Page Object Model (POM)

Separates UI logic from test logic for better maintainability.

### Test Data Separation

Test data is separated from test logic to improve scalability.

### Popup Handling Strategy

Handles Samsung Pass popup to prevent test interruption.

### Test Parameterization

Executes test scenarios using pytest parameterization.

```python
@pytest.mark.parametrize("set_name, case", test_params)
```

---

## ⚙️ Test Execution Strategy

Tests are categorized using pytest markers:

* `@pytest.mark.device` → Mobile tests (real device required)
* Non-marked tests → CI-safe tests

This enables:

* Fast validation in CI
* Full test execution in local environments

---

## 🔄 Test Flow

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

## ✅ Test Scenarios

* Login attempt without entering credentials
* Login attempt with phone number only
* Login attempt with password only
* Login attempt with valid credentials

---

## 🛠️ Prerequisites

* Python 3.9+
* Appium Server
* Android SDK
* Node.js (for Appium)
* Connected Android device

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Edit values in `config.py` if needed:

* DEVICE_NAME
* APP_PACKAGE
* APP_ACTIVITY

Example:

```python
options.set_capability("deviceName", "AndroidDevice")
```

---

## ▶️ Run Tests

### Run all tests

```bash
pytest -v
```

### Run CI-safe tests

```bash
pytest -m "not device"
```

### Run mobile tests

```bash
pytest -m device
```

---

## 🤖 CI & Reporting

This project integrates **GitHub Actions + Allure Reports**.

### CI Pipeline

* Runs on every push and pull request
* Executes non-device tests only:

```bash
pytest -m "not device"
```

* Generates Allure test reports automatically

### Report Deployment

* CI reports → `/ci`
* Mobile reports → `/mobile`
* Hosted via GitHub Pages

> Device tests are excluded from CI due to real device requirements.

---

## 📄 Logging

```
2026-03-12 16:00:21 [INFO] [START] SET1_CASE1 - 로그인 정보 미입력
```

---

## 🚧 Planned Improvements

* Explore mock-based testing for faster CI validation
* Improve CI coverage with additional test scenarios
* Enhance test reporting with more detailed metadata
