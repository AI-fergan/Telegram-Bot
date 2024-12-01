import json

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

#bot settings
BOT_NAME = data["Name"]
USERNAME = data["UserName"]
TOKEN = data["Token"]
DOWNLOADS = data["Downloads"]
