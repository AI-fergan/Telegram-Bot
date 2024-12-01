import json

with open("config.json", "r") as json_data_file:
    data = json.load(json_data_file)

#Testers settings
platformName = data["platformName"]
platformVersion = data["platformVersion"]
deviceName = data["deviceName"]
automationName = data["automationName"]
ensureWebviewsHavePages = data["ensureWebviewsHavePages"]
nativeWebScreenshot = data["nativeWebScreenshot"]
newCommandTimeout = data["newCommandTimeout"]
connectHardwareKeyboard = data["connectHardwareKeyboard"]        
Remote = data["Remote"]     
