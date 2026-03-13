from appium.options.android import UiAutomator2Options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

APP_PACKAGE = "com.tossplace.app.release"
APP_ACTIVITY = "com.tossplace.app.androidPos.IntroActivity"

DEFAULT_WAIT = 10

def get_driver_options():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "AndroidDevice")
    options.set_capability("appPackage", APP_PACKAGE)
    options.set_capability("appActivity", APP_ACTIVITY)
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)
    return options

