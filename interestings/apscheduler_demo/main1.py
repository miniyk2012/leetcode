# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test(x):
    print(1 / 0)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')

    scheduler.start()
