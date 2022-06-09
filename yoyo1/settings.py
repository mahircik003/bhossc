from pathlib import Path
import os
import django_heroku
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #os.environ.get('DEBUG') == 'True' # os.environ.get("DEBUG", "False") == "True" 

ALLOWED_HOSTS = ['bhos.svdev.me', 'admin.svdev.me', '127.0.0.1', 'localhost', '.herokuapp.com', 'bhossc.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'channels',
    'chat',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework', 
    'base.apps.BaseConfig',
    'last_visit.apps.LastVisitConfig',
    'cloudinary',
    # 'django_extensions',
]

AUTH_USER_MODEL = 'base.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'last_visit.middleware.LastVisit',
]
    

# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:8000/api/rooms'
# ]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'yoyo1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'yoyo1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': { 
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    # for development
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bhossc',
        'USER': 'postgres',
        'PASSWORD': 'asdfg122',
        # 'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': '5432', 
    }    

    # for production
    # 'default' : {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'd6bg7o0gl5qv4l',
    #     'USER': os.environ.get('DATABASE_USER'),
    #     'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
    #     'HOST': os.environ.get('DATABASE_HOST'),
    #     'PORT': '5432', 
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = BASE_DIR / 'static/images'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'email_backend.DKIMBackend'
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'  # Gmail’s SMTP server == domain name
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "pltrfstd@gmail.com"
# EMAIL_HOST_PASSWORD = "topcxyrwqvlyqhzh"

ASGI_APPLICATION = "yoyo1.asgi.application"

# DO NOT UNCOMMENT CODE COMMENTED BELOW
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
#         },
#     },
# }


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

cloudinary.config( 
  cloud_name = "dn3laf4bh", 
  api_key = "458123621829519", 
  api_secret = "Mri5UR7onSpyBvRf7HePmq7K1ug" 
)
