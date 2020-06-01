import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "doodle_server",
        "USER": "admin",
        "PASSWORD": "rlagkwjd0318",
        "HOST": "doodle-server.cicwjfqhynn6.ap-northeast-2.rds.amazonaws.com",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}