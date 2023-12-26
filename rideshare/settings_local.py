from rideshare.settings import *

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0', 'http://127.0.0.1', 'http://localhost']
STATIC_ROOT = "/static/"

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers

    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },

    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "/var/log/django/general.log",
            "level": "DEBUG",
            "formatter": "verbose"
        },
    },

    "formatters": {
        "verbose": {
            "format": '{{"component": "$name"} {"level": "$levelname"} {"timestamp": "$asctime"} {"module": "$module"} {"process": "$process:d"} {"thread": "$thread:d"} {"message": "$message"}',
            "style": "$",
        }
    },
}