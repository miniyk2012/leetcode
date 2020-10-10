from celery import Celery

cel = Celery('celery_demo',
             broker='redis://127.0.0.1:6379/2',
             backend='redis://127.0.0.1:6379/1',
             # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['celery_tasks.task01',
                      'celery_tasks.task02'
                      ])

# 时区
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc = False


# celery -A celery_tasks worker -l INFO -P eventlet