from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import config

def Test(driver: webdriver.Remote):
    """
    This Tester check if bot send Error message when the user send text.
    """
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")').click()
    sleep(0.1)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView').click()

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Search")').send_keys(config.USERNAME)

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + config.USERNAME + '")').click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Message")').send_keys("Test 2")

    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Send")').click()
    sleep(0.1)

    #get the last message
    elements = driver.find_elements(AppiumBy.XPATH, f"//*[contains(@text, '{config.BOT_NAME}')]")

    return str(elements[-1].text).split(": ")[0] == config.BOT_NAME + " ERROR"
