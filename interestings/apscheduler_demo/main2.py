# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def aps_pause(x):
    scheduler.pause_job('interval_task')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def aps_resume(x):
    scheduler.resume_job('interval_task')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/2', id='cron_task')
    scheduler.add_job(func=aps_pause, args=('一次性任务,停止循环任务',),
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12), id='pause_task')
    scheduler.add_job(func=aps_resume, args=('一次性任务,恢复循环任务',),
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=29), id='resume_task')
    scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=2, id='interval_task')

    scheduler.start()
