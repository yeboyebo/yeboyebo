from os import path
import sys

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

sys.path.insert(0, path.join(PROJECT_ROOT, "../../../motor/"))
sys.path.insert(1, path.join(PROJECT_ROOT, "apps/"))

from YBAQNEXT.settings import *
from YBAQNEXT.yeboapps import *

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Madrid'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_rabbitmq.RabbitmqChannelLayer',
        'ROUTING': 'AQNEXT.routing.channel_routing',
        'CONFIG': {
            'url': 'amqp://desarrollo:desarrollo@localhost:5672/desarrollo'
        },
    },
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += ('djangosecure', 'channels', )

MIDDLEWARE_CLASSES += (
    'djangosecure.middleware.SecurityMiddleware',
)

from .local import *
