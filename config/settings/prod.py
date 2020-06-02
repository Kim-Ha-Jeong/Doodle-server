import json
import os
from .base import *
#import sentry_sdk 에러 내용 찾아줌
#from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False # 꼭 필요합니다.

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = secrets['DB_SETTINGS']