"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path, os
from dotenv import load_dotenv
load_dotenv()
from django.core.management.utils import get_random_secret_key

MYSQL_DATABASE_NAME = os.environ.get('MYSQL_DATABASE_NAME')
MYSQL_DATABASE_USER = os.environ.get('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_HOST = os.environ.get('MYSQL_DATABASE_HOST')
MYSQL_DATABASE_PORT = os.environ.get('MYSQL_DATABASE_PORT') 
MYSQL_DATABASE_TIME_ZONE = os.environ.get('MYSQL_DATABASE_TIME_ZONE') 
#************************************************************************
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS'] == 'True'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')
#************************************************************************
SECRET_KEY = os.environ.get('SECRET_KEY') 
#************************************************************************
DEBUG = os.environ['DEBUG'] == 'True'
ALLOWED_HOSTS = os.environ.get('SERVERNAMES').split(' ')
#************************************************************************

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()
# SECRET_KEY = 'django-insecure-86=ieah6_s6=#4i_yu=pqk!h3)7w9wrr4vfc&77slmx!5evjye'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'errorPage.apps.ErrorpageConfig',
    'account.apps.AccountConfig',
    'adminManage.apps.AdminmanageConfig',
    'tailwind',
    'theme',
    # 'django_browser_reload', # Reload browser automatically

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_browser_reload.middleware.BrowserReloadMiddleware', # Reload browser automatically
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        # 'DIRS': [BASE_DIR / 'account/templates', BASE_DIR /'theme/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

TAILWIND_APP_NAME = 'theme'

# For developer mode
INTERNAL_IPS = [
    "127.0.0.1",
]
AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

PASSWORD_RESET_TIMEOUT = 300 # 5 minutes

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DATABASE_NAME,
        'USER': MYSQL_DATABASE_USER,
        'PASSWORD': MYSQL_DATABASE_PASSWORD,
        'HOST': MYSQL_DATABASE_HOST,
        'PORT': MYSQL_DATABASE_PORT,
        'TIME_ZONE': MYSQL_DATABASE_TIME_ZONE,
        'default-character-set' : 'utf8',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'TH'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = 'singin'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# กรณีมีอยู่ที่อื่นๆ ให้เพิ่มที่นี่
STATICFILES_DIRS = [
    # BASE_DIR / "app/static",
    BASE_DIR / "static",
]


# Email protocol
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
SERVER_EMAIL = SERVER_EMAIL

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
