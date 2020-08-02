"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from os import getenv
from pathlib import Path

import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as _settings

PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()

SECRET_KEY = _settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS + ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS_ORDERED = {
    0: "django.contrib.admin",
    10: "django.contrib.auth",
    20: "django.contrib.contenttypes",
    30: "django.contrib.sessions",
    40: "django.contrib.messages",
    50: "django.contrib.staticfiles",
    60: "rest_framework",
    70: "django.contrib.sites",
    80: "drf_yasg",
    90: "storages",
    100: "django.contrib.gis",
    # --- my applications ---
    1000: "apps.onboarding.apps.OnboardingConfig",
    2000: "apps.index.apps.IndexConfig",
    3000: "apps.vietnam.apps.VietnamConfig",
    4000: "apps.blog.apps.BlogConfig",
    5000: "apps.api.apps.ApiConfig",
    6000: "apps.contacts.apps.ContactsConfig",
    7000: "apps.preparation.apps.PreparationConfig",
}

INSTALLED_APPS = [app for _, app in sorted(INSTALLED_APPS_ORDERED.items())]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates",],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = getenv("DATABASE_URL")

DATABASES = {
    # 'default': {
    # "ENGINE": "django.db.backends.sqlite3",
    # "NAME": (BASE_DIR / "db.sqlite3").as_posix(),
    # }
    "default": dj_database_url.parse(_db_url, conn_max_age=600)
}
DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

# AUTH_PASSWORD_VALIDATORS = [
# { "NAME": "django.contrib.login.password_validation.UserAttributeSimilarityValidator",},
# {"NAME": "django.contrib.login.password_validation.MinimumLengthValidator", },
# {"NAME": "django.contrib.login.password_validation.CommonPasswordValidator", },
# {"NAME": "django.contrib.login.password_validation.NumericPasswordValidator", },
# ]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/assets/"

STATICFILES_DIRS = [PROJECT_DIR / "static"]

STATIC_ROOT = REPO_DIR / ".static"

if not DEBUG:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://cc746b5c10374d00a93041cf5a1caeb1@o383048.ingest.sentry.io/5212817",
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.login) you may enable sending PII data.
        send_default_pii=True,
    )
EMAIL_HOST = _settings.EMAIL_HOST
EMAIL_HOST_PASSWORD = _settings.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = _settings.EMAIL_HOST_USER
EMAIL_PORT = _settings.EMAIL_PORT
EMAIL_USE_SSL = _settings.EMAIL_USE_SSL
EMAIL_USE_TLS = _settings.EMAIL_USE_TLS
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_FROM = _settings.EMAIL_FROM

LOGIN_URL = reverse_lazy("onboarding:sign_in")
LOGIN_REDIRECT_URL = reverse_lazy("onboarding:me")

SITE_ID = _settings.SITE_ID

AWS_ACCESS_KEY_ID = _settings.AWS_ACCESS_KEY_ID
AWS_DEFAULT_ACL = "public-read"
AWS_LOCATION = _settings.AWS_LOCATION
AWS_QUERYSTRING_AUTH = False
AWS_S3_ADDRESSING_STYLE = "path"
AWS_S3_REGION_NAME = _settings.AWS_S3_REGION_NAME
AWS_SECRET_ACCESS_KEY = _settings.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = "travel-taranova"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header",}
    },
}
ADMIN_MEDIA_PREFIX = "/static/admin/"
