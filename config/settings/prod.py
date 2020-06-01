import json
import os
from .base import *
#import sentry_sdk 에러 내용 찾아줌
#from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False  # 꼭 필요합니다.

with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'secrets.json', 'rb', encoding = 'utf-8') as secret_file:
    secrets = json.load(secret_file)

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']
}