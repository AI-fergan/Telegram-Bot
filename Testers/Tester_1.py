from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import config

def Test(driver: webdriver.Remote):
	"""
	This Tester check if the bot return the md5 hash of image in jpg / jpeg 
	"""
	driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")').click()

	driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView').click()

	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Search")').send_keys(config.USERNAME)

	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + config.USERNAME + '")').click()
	sleep(0.1)
	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Attach media")').click()
	sleep(0.2)
	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("File")').click()

	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gallery").instance(0)').click()
	sleep(0.1)
	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)').click()

	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show as list")').click()

	recycler_view = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("androidx.recyclerview.widget.RecyclerView")')

	#choose image in jpg format from the gallery
	elements = recycler_view.find_elements(AppiumBy.XPATH, "//*")
	for element in elements:
		if element.text.endswith(".jpg"):
			element.click()

	element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)').click()
	sleep(0.2)	

	#get the last message
	elements = driver.find_elements(AppiumBy.XPATH, f"//*[contains(@text, '{config.BOT_NAME}')]")

	return str(elements[-1].text).split(": ")[0] == config.BOT_NAME + " md5"