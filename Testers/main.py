import Tester_1, Tester_2, Tester_3
from appium import webdriver
from appium.options.common.base import AppiumOptions
import config
def getDriver():
    """
    This function configure the driver settings and return it.
    """
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": config.platformName,
        "appium:platformVersion": config.platformVersion,
        "appium:deviceName": config.deviceName,
        "appium:automationName": config.automationName,
        "appium:ensureWebviewsHavePages": config.ensureWebviewsHavePages,
        "appium:nativeWebScreenshot": config.nativeWebScreenshot,
        "appium:newCommandTimeout": config.newCommandTimeout,
        "appium:connectHardwareKeyboard": config.connectHardwareKeyboard
    })

    return webdriver.Remote(config.Remote, options=options)


def main():
    driver = getDriver()
    valid = True

    print("[*] Tester start...")
    #Valid image Test
    if Tester_1.Test(driver):
        print("Test 1 Passed")
    else:
        print("Test 1 Faild")
        valid = False

    driver.keyevent(4)
    driver.keyevent(4)

    #Not valid text Test
    if Tester_2.Test(driver):
        print("Test 2 Passed")
    else:
        print("Test 2 Faild")
        valid = False
    

    driver.keyevent(4)
    driver.keyevent(4)

    #Not valid image Test
    if Tester_3.Test(driver):
        print("Test 3 Passed")
    else:
        print("Test 3 Faild")
        valid = False

    print("[*] Tester finish")

    #Check if the bot passed all the tests
    if valid:
        print("[*] The bot is working ok!")
    else:
        print("[*] The bot failed :(")
    

if __name__ == "__main__":
    main()