import json
import datetime as dt
import requests
import slack

def lambda_handler(event, context):
  # Open Weather Map API Key
  weather_key = "****"

  city_name = "Kyoto"
  weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric"
  weather_url = weather_url.format(city = city_name, key = weather_key)
  # AWS Lambda は UST なので JST に変える
  time = dt.datetime.now()
  time += dt.timedelta(hours=9)
  time = time.hour

    # 天気データを取得
  weather_req = requests.get(weather_url)
  weather_data = json.loads(weather_req.text)
  weather_id = weather_data["weather"][0]["id"]


  # weather id をもとに分類
  if weather_id == 800 or weather_id == 801:
    if (time >= 19 and time <= 23) or (time >= 0 and time <= 4):
      weather = slack.Status("晴れ", ":star:")
    else:
      slack.Status("晴れ", ":sunny:")
  elif weather_id >= 802 and weather_id <= 804:
    weather = slack.Status("曇り", ":cloud:")
  elif weather_id >= 300 and weather_id <= 321:
    weather = slack.Status("霧", ":droplet:")
  elif weather_id >= 500 and weather_id <= 531:
    weather = slack.Status("雨", ":umbrella:")
  elif weather_id >= 200 and weather_id <= 232:
    weather = slack.Status("雷", ":zap:")
  elif weather_id >= 600 and weather_id <= 622:
    weather = slack.Status("雪", ":snowflake:")
  elif weather_id >= 900:
    weather = slack.Status("風", ":cyclone:")
  
  weather.change()
  
  return "ok"
