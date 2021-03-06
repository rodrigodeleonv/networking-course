"""
Django settings for redes project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import re
import json
from socket import gethostname

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_PATH = os.path.join(BASE_DIR, 'redes', 'environconf', 'config.json')

with open(CONFIG_PATH, 'r') as config_file:
    conf = json.load(config_file)

# Setting the environment settings
hostame_regex = re.compile(r'^I\d{1,2}$')  # I0, I1, I2, ..., I99
if hostame_regex.match(gethostname()):
    conf_en = conf['production']
else:
    conf_en = conf['local']

SECRET_KEY = conf_en['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf_en['DEBUG']

ALLOWED_HOSTS = ['rodrigodeleon.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Thrid apps
    'django_extensions',
    'widget_tweaks',
    # My apps
    'users',
    'web',
    'homework',
    'reporters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'redes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'project_templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'redes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_L10N = True
# DECIMAL_SEPARATOR = '.'

USE_TZ = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'web:home'
LOGOUT_REDIRECT_URL = 'login'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC_ROOT')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_dir'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'MEDIA_ROOT')


# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'account@domain.com'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_USE_TLS = True

AUTH_USER_MODEL = 'users.User'
