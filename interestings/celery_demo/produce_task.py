import time
from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg

from celery.result import AsyncResult
from celery_tasks.celery import cel

# 立即告知celery去执行test_celery任务，并传入一个参数
result = send_email.delay('yuan')
id1 = result.id
print(id1)
result2 = send_msg.delay('mniubi')
id2 = result2.id
print(id2)

async_result = AsyncResult(id=id2, app=cel)

while True:
    if async_result.successful():
        result = async_result.get()
        print(result)
        break
        # result.forget() # 将结果删除,执行完成，结果不会自动删除
        # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
        # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
    elif async_result.failed():
        print('执行失败')
    elif async_result.status == 'PENDING':
        print('任务等待中被执行')
    elif async_result.status == 'RETRY':
        print('任务异常后正在重试')
    elif async_result.status == 'STARTED':
        print('任务已经开始被执行')
    time.sleep(1)



