import requests
import json

USER_TOKEN = "*********************"
USER_ID = "*******" 

class Status:

  def __init__(self, text, emoij):
    self.text = text
    self.emoji = emoij

    self.date = {}

  def change(self):
    self.data = {
    "token" : USER_TOKEN,
    "user": USER_ID,
    "profile":json.dumps({
        "status_text":self.text,
        "status_emoji":self.emoji
        })
    }
    requests.post('https://slack.com/api/users.profile.set',params = self.data)
