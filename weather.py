## Open Weather Mapを使って天気を取得しstatus emojiを変更する

import json
import csv
import datetime as dt
import requests
import slack

def get_weather():
  # Open Weather MapにログインしてAPI Keyを取得する
  weather_key = "***********"

  # 都市名。今回は京都
  city_name = "Kyoto"

  url = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric"
  weather_url = url.format(city=city_name, key=weather_key)
  
  # AWS Lambda は UST なので、JST を UST に変える
  time = dt.datetime.now() + dt.timedelta(hours=9) 
  time = time.hour

  # 天気データを取得
  weather_req = requests.get(weather_url)
  weather_data = json.loads(weather_req.text)
  weather_id = weather_data["weather"][0]["id"]
  
  # csvファイルを読み込む
  with open('weather_data.csv', 'r') as f:
    csvdata = csv.reader(f)
    # 配列に格納する
    data = [x for x in csvdata]

  # 辞書型に整形
  get_data = dict(data)

  # weather id をもとに分類し、textとemojiを代入
  if weather_id == 800 or weather_id == 801:
    # 夜間
    if (time >= 19 and time <= 23) or (time >= 0 and time <= 4):
      now_weather = slack.Status(get_data[str(weather_id)], ":star:")
    else:
      slack.Status(get_data[str(weather_id)], ":sunny:")
  elif weather_id >= 802 and weather_id <= 804:
    now_weather = slack.Status(get_data[str(weather_id)], ":cloud:")
  elif weather_id >= 300 and weather_id <= 321:
    now_weather = slack.Status(get_data[str(weather_id)], ":droplet:")
  elif weather_id >= 500 and weather_id <= 531:
    now_weather = slack.Status(get_data[str(weather_id)], ":umbrella:")
  elif weather_id >= 200 and weather_id <= 232:
    now_weather = slack.Status(get_data[str(weather_id)], ":zap:")
  elif weather_id >= 600 and weather_id <= 622:
    now_weather = slack.Status(get_data[str(weather_id)], ":snowflake:")
  elif weather_id >= 900:
    now_weather = slack.Status(get_data[str(weather_id)], ":cyclone:")
  else:
    now_weather = slack.Status(get_data[str(weather_id)], ":astonished:")

  # status emojiを変更する
  now_weather.change()
  # 確認のためターミナルに出力
  print(weather_id)
