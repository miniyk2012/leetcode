import time
from celery.result import AsyncResult

from celery_task import cel
from celery_task import send_email

result = send_email.delay("yuan")
id1 = result.id
print(id1)
result2 = send_email.delay("alex")
id2 = result2.id
print(id2)

async_result = AsyncResult(id=id1, app=cel)
while True:
    if async_result.successful():
        result = async_result.get()
        print(result)
        break
    elif async_result.failed():
        print('执行失败')
    elif async_result.status == 'PENDING':
        print('任务等待中被执行')
    elif async_result.status == 'RETRY':
        print('任务异常后正在重试')
    elif async_result.status == 'STARTED':
        print('任务已经开始被执行')
    time.sleep(1)
