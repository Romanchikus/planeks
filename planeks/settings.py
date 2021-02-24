import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%kzwttsu_@q(r#h6bx9fzrty&-+r460h1%m6fq%5(p-!+-zm^o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['planeks13.herokuapp.com','https://planeks13.herokuapp.com/','http://planeks13.herokuapp.com/','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'schemas',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'planeks.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'planeks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

ON_HEROKU = os.environ.get("ON_HEROKU")
if ON_HEROKU:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    db_from_env = dj_database_url.config(
        default=DATABASE_URL, conn_max_age=500, ssl_require=True
    )
else:
    DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500)
DATABASES = {"default": db_from_env}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AUTH_USER_MODEL = "User"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

if ON_HEROKU:
    REDIS_URL = os.environ.get("REDIS_URL")
    CELERY_BROKER_URL = REDIS_URL  
    CELERY_RESULT_BACKEND = REDIS_URL
else:
    CELERY_BROKER_URL = 'redis://localhost:6379'  
    CELERY_RESULT_BACKEND = 'redis://localhost:6379' 

 
CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TASK_SERIALIZER = 'json'  