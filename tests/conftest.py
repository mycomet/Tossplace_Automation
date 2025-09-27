# 테스트 공통 설정 (pytest fixture)

import pytest
import subprocess
import time
import os
import signal
import psutil
from appium import webdriver
from config import get_driver_options

@pytest.fixture(scope="session")
def appium_server():
    "Appium 서버 실행 및 종료 관리"
    
    appium_path = os.environ.get(
    "PATH_APPIUM",
    os.path.expandvars(r"%APPDATA%\npm\appium.cmd")  # 사용자에 따라 appium 실행 경로 자동 설정
    )
    
    # Appium 서버 실행
    server = subprocess.Popen(
        [appium_path, "--allow-cors"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    print("Appium 서버 실행 중... 대기")
    time.sleep(5)

    yield

    print("Appium 서버 종료 중...")
    try:
        if psutil.pid_exists(server.pid):
            if os.name == "nt": # 윈도우 사용시 
                subprocess.run(["taskkill", "/F", "/PID", str(server.pid)], check=True)
            
            else: # 윈도우 아닌 경우 (Mac/Linux)
                os.kill(server.pid, signal.SIGTERM) 
            print("Appium 서버 종료 완료")
        else:
            print("Appium 서버가 이미 종료됨")
    except Exception as e:
        print(f"서버 종료 실패: {e}")

@pytest.fixture(scope="session")
def driver(appium_server):
    "Appium 드라이버 세션 생성 및 종료"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=get_driver_options())

    driver.terminate_app("com.tossplace.app.release")
    driver.activate_app("com.tossplace.app.release")
    time.sleep(10)

    yield driver

    time.sleep(10)
    driver.quit()
