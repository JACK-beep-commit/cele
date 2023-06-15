from celery import Celery
import os
import django
from django.conf import settings

# 设置环境变量和djcelery工作目录
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_task.settings")
django.setup()

# 实例化应用,工程名字
celery_app = Celery('djangoProject1')

# 读取celery的配置
celery_app.config_from_object(settings)

# 如果项目中有task.py, 那么使用celery_app项目中的task来生成任务
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
