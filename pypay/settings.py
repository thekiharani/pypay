import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'n^l4-rdwss#c3i%j+$y=8my-=^gdk_x-22*g$ga!8y+q@e#exu')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') == '1' else False

ALLOWED_HOSTS = ['*'] if os.environ.get('DEBUG') == '1' else ['maishabeta.com', '161.35.149.26']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    # local
    'accounts.apps.AccountsConfig',
    'daraja.apps.DarajaConfig',

    # third party
    'rest_framework',

    # local
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Custom Config
AUTH_USER_MODEL = 'accounts.User'
# CRISPY_TEMPLATE_PACK = 'bootstrap4'
# LOGIN_REDIRECT_URL = 'maisha:home'
# LOGOUT_REDIRECT_URL = 'maisha:home'
# TOS = 'http://TOS'

DARAJA_CONSUMER_KEY = os.environ.get('DARAJA_CONSUMER_KEY')
DARAJA_CONSUMER_SECRET = os.environ.get('DARAJA_CONSUMER_SECRET')
DARAJA_SHORT_CODE = os.environ.get('DARAJA_SHORT_CODE')
DARAJA_LIPA_ONLINE = os.environ.get('DARAJA_LIPA_ONLINE')
DARAJA_PASSKEY = os.environ.get('DARAJA_PASSKEY')
DARAJA_PHONE_NUMBER = os.environ.get('DARAJA_PHONE_NUMBER')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pypay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pypay.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_NAME = os.environ.get('DATABASE_NAME', '')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', '')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'postgres')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USERNAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },

    'sqlite': {
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_ACCESS_SECRET', '')
AWS_STORAGE_BUCKET_NAME = 'maishabeta-space'
AWS_S3_ENDPOINT_URL = 'https://ams3.digitaloceanspaces.com'
# AWS_S3_CUSTOM_DOMAIN = 'ams3.cdn.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'thekiharani'
AWS_DEFAULT_ACL = 'public-read'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = '{}/{}/' .format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}