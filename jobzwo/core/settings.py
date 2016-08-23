# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from core.bootstrap import setup_structlog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u9a%l0^^-rh$w4xairfsb#xl^(1+g$qoy)r0vk=gcd3a+pj3@q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TESTING = (len(sys.argv) > 1 and sys.argv[1] == 'test')

ALLOWED_HOSTS = []
INTERNAL_IPS = [
    '192.168.50.50'
]

DEBUG_TOOLBAR_ENABLED = False
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Application definition

INSTALLED_APPS = (
    'core',

    'debug_toolbar',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'core.middleware.StructLoggingMiddleware',
    'core.middleware.ExceptionLoggingMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


if DEBUG_TOOLBAR_ENABLED:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE_CLASSES += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]


ROOT_URLCONF = 'jobzwo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'core.context_processors.contact_email',
                'core.context_processors.site_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': 'jobzwo.sqlite',
        #'USER': 'jobzwo',
        #'PASSWORD': 'jobzwo',
        #'HOST': '127.0.0.1',

        #'CONN_MAX_AGE': 500,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_ROOT = os.path.join(BASE_DIR, 'upload', '')
MEDIA_URL = '/upload/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CONTACT_EMAIL = 'stephan.poetschner+jobzwo@gmail.com'
DEFAULT_FROM_EMAIL = CONTACT_EMAIL  # where emails (via send_mail) come from
SERVER_EMAIL = CONTACT_EMAIL  # where error messages will come from

ADMINS = (
    ('Stephan Poetschner', 'stephan.poetschner+jobzwo@gmail.com'),
)
MANAGERS = ADMINS

LOGGING_PREFIX = 'jobzwo.'

# Logging
setup_structlog()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_testing_false': {
            '()': 'core.utils.RequireTestingFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_testing_false'],
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_testing_false', 'require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console',],
            'level': 'INFO',
        },
        'py.warnings': {
            'handlers': ['console'],
            'level': 'WARN',
            'propagate': False,
        },
        'requests': {
            'handlers': ['console'],
            'level': 'WARN',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
