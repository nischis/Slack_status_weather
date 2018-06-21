## 10分ごとに天気を取得し変更する。このファイルを実行する。

from apscheduler.schedulers.blocking import BlockingScheduler
import weather

# スケジューラー
sched = BlockingScheduler()

# 10の倍数分に天気を取得しそれぞれ変更する
@sched.scheduled_job("cron", minute="0,10,20,30,40,50")
def scheduled_job():
  weather.get_weather()

# スケジューラー開始
sched.start()