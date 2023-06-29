"""
Django settings for quanlydoan project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import pymysql
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^&-6n^1-v(!7z3o-q0f628!e%^ws^$r)!(4^2rq_gxv&m5y7tc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'djoser',
    'frontend.apps.FrontendConfig'
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

ROOT_URLCONF = 'quanlydoan.urls'

# TODO: check the build for later debugging
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'quanlydoan.wsgi.application'

#install pymsql for Mysql Db
pymysql.version_info = (2, 1, 1, "final", 0)
pymysql.install_as_MySQLdb()

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projectmanager',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'DucPhuc2',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Source: https://djoser.readthedocs.io/en/latest/authentication_backends.html
# Add rest_framework_simplejwt.authentication.JWTAuthentication to 
# Django REST Framework authentication strategies tuple:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':{
        'rest_framework.permissions.IsAuthenticated'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configure django-rest-framework-simplejwt to use the Authorization: JWT
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

# email set up for django
# USING SMTP PROTOCOL FOR AUTHENICATION

EMAIL_BACKEND  = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'tserverside@gmail.com'
EMAIL_HOST_PASSWORD = 'xx`5aO]-ZuJBqyRh'
EMAI_USE_TLS = True


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# TODO: check the Build from the template too
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend\static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Setup Djoser setting for Djoser API
# Src: https://djoser.readthedocs.io/en/latest/settings.html#

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE' : True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION' : True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' : True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_PASSWORD_RETYPE' : True,
    'PASSWORD_RESET_CONFIRM_URL' : 'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS' : {
        'user_create' : 'api.serializers.UserCreateSerializer',
        'user' : 'api.serializers.UserCreateSerializer',
        'user_delete' : 'api.serializers.UserDeleteSerializer',
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Use custom user model as default 
AUTH_USER_MODEL = 'api.UserAccount'