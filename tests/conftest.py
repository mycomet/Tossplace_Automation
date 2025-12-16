
import pytest
import subprocess
import time
import os
import signal
import psutil
import logging, sys
from appium import webdriver
from config import get_driver_options
from pages.login_page import TossplacePage

# 1) Appium 서버 실행
@pytest.fixture(scope="session")
def appium_server():
    # Appium 경로 설정 (사용자에 따라 경로 자동 설정)
    logging.info("[INIT] Launching Appium Server...")
    appium_path = os.environ.get(
        "PATH_APPIUM",
        os.path.expandvars(r"%APPDATA%\npm\appium.cmd")
    )

    # Appium 서버 실행
    if sys.platform.startswith("win"): # Windows
        creationflags = subprocess.CREATE_NEW_CONSOLE
    else: # Mac/Linux
        creationflags = 0

    server = subprocess.Popen(
        [appium_path, "--allow-cors"], 
        creationflags=creationflags
        )
    
    logging.info("[INIT] Appium Server Started Successfully")
    time.sleep(5)

    yield

    # Appium 서버 종료
    logging.info("[TEARDOWN] Stopping Appium Server...")

    try:
        server_pid = getattr(server, "pid", None)

        if server_pid and psutil.pid_exists(server.pid):
            if os.name == "nt": # Windows
                subprocess.run(["taskkill", "/F", "/PID", str(server.pid)], check=True)
            
            else: # Mac/Linux
                os.kill(server.pid, signal.SIGTERM)

            time.sleep(1)
            logging.info("[TEARDOWN] Appium server stopped successfully")

        else:
            logging.info("[WARN] Appium server already stopped")

    except Exception as e:
        print(f"[ERROR] Exception while stopping Appium server: {e}")

# 2) 드라이버 생성
@pytest.fixture(scope="session")
def driver(appium_server):

    # Appium 드라이버 세션 생성
    logging.info("[SETUP] Creating Appium Driver Session...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=get_driver_options())

    yield driver
    logging.info("[TEARDOWN] Closing Appium Driver Session...")

    time.sleep(10)
    driver.quit()
    logging.info("[TEARDOWN] Driver Session Closed Successfully")

# 3) 세트 전환 감지 후 리셋
@pytest.fixture(autouse=True)   # True -> set전환시 reset 위함
def reset_between_sets(request, driver):
    callspec = getattr(request.node, "callspec", None)
    set_name = None

    if callspec:
        set_name = callspec.params.get("set_name")

    prev = getattr(request.session, "last_set_name", None)

    # 각 set의 case1 진행 전에 reset 수행
    if set_name and prev != set_name:
        prev_label = prev if prev is not None else "INIT"
        logging.info(f"[RESET] Switching from {prev_label} → {set_name}")
        
        driver.terminate_app("com.tossplace.app.release")
        driver.activate_app("com.tossplace.app.release")
        time.sleep(10)

    if set_name:
        request.session.last_set_name = set_name

    yield

# 4) Page Object 제공
@pytest.fixture(scope="function")
def page(driver):
    return TossplacePage(driver)

# 5) 로그인 화면 보장 precondition
@pytest.fixture(scope="function", autouse=True)
def ensure_login_screen(page, reset_between_sets):

    if not page.on_login_screen():
        # 로그인 화면이 아니면, ACTION을 기록하고 이동
        logging.info("[ACTION] Navigating to login screen.")
        page.go_to_login_screen()

    else:
        # 로그인 화면인 것이 확인되면, INFO 로그를 기록하고 유지
        logging.info("[INFO] Login screen confirmed.")
    return page

