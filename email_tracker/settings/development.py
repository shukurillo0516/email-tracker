import os
from email_tracker.settings.base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:5050"]
CORS_ALLOWED_ORIGIN_REGEXES = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "pass"),
        "HOST": os.environ.get("DB_HOST", "tezdb"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
