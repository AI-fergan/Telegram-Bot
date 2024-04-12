from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def Test(driver: webdriver.Remote):
    """
    This Tester check if cyberat bot send Error message when the user send text.
    """
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")').click()
    sleep(0.1)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView').click()

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Search")').send_keys("imcyberat_bot")

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CybeRat, bot")').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Message")').send_keys("Test 2")

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Send")').click()
    sleep(0.1)

    #get the last message
    pattern = "cyberat"
    elements = driver.find_elements(AppiumBy.XPATH, f"//*[contains(@text, '{pattern}')]")

    return str(elements[-1].text).split(": ")[0] == "cyberat ERROR"
