
from appium.options.android import UiAutomator2Options

def get_driver_options():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "R3CT90HV2YH")
    options.set_capability("appPackage", "com.tossplace.app.release")
    options.set_capability("appActivity", "com.tossplace.app.androidPos.IntroActivity")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)  # 앱 초기화 방지
    return options
