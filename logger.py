# sistema de logs
from logging.config import dictConfig
import logging
import os

log_path = "log/"
if not os.path.exists(log_path):
   os.makedirs(log_path)

dictConfig({
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)-4s %(funcName)s() L%(lineno)-4d %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "log/app.log",
            "maxBytes": 10000000,
            "backupCount": 5,
        }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    }
})

logger = logging.getLogger(__name__)