from .base import *
import os

DEBUG = False
SECRET_KEY=os.environ["SECRET_KEY"]
ALLOWED_HOSTS=["*"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

CSRF_TRUSTED_ORIGINS = [
    'https://cms.beijing.academy',
    'http://localhost:3000',
]

try:
    from .local import *
except ImportError:
    pass
