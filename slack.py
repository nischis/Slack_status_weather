## status emojiを変更する

import requests
import json

# SlackのLegacy Tokensから取得する
USER_TOKEN = "xoxp-****"
# Slackのusers.list methodsでTest methodして取得
USER_ID = "*******" 

class Status:

  # 天気にあったテキストと絵文字を取得
  def __init__(self, text, emoij):
    self.text = text
    self.emoji = emoij
    self.date = {}

  def change(self):
    
    # 必要な情報をdata格納する
    self.data = {
    "token" : USER_TOKEN,
    "user": USER_ID,
    "profile":json.dumps({
        "status_text":self.text,
        "status_emoji":self.emoji
        })
    }
    # HTTPリクエストでdataをポストする
    requests.post('https://slack.com/api/users.profile.set',params = self.data)
