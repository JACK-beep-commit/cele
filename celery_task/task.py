from __future__ import absolute_import
from djangoProject1.celery import celery_app


@celery_app.task
def say_hello(number):
    print("11111111111111111number: {}".format(number))

@celery_app.task
def say_hello2():
    print("1111111111111113333311number")