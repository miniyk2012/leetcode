import time
from celery_tasks.celery import cel

@cel.task
def add(a, b):
    return a+b


@cel.task
def mul(a, b):
    return a * b