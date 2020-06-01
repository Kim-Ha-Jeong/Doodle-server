import json
import os
from .base import *
#import sentry_sdk 에러 내용 찾아줌
#from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False  # 꼭 필요합니다.
dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'secrets.json')
with open(dir, 'rb') as secret_file:
    secrets = json.load(secret_file)

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

DATABASES = {
    'default': secrets['DB_SETTINGS']
}