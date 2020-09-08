"""
Django settings for DjangoWebProject3 project.
"""
from __future__ import absolute_import, unicode_literals
import os
import django.contrib.auth
import django_pesapal
# import djcelery
# djcelery.setup_loader()
# BROKER_URL = 'amqp://guest:guest@localhost:5672'
# from django.core.checks import templates
django.contrib.auth.LOGIN_URL = '/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

LOGIN_URL ='/login/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# CELERY_RESULT_BACKEND = 'django-db'

# CELERY_RESULT_BACKEND = 'django-cache'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # Not used with sqlite3.
        'USER': '',
        # Not used with sqlite3.
        'PASSWORD': '',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}#redis configurations

# BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Africa/Nairobi'
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Nairobi'


# ALLOWED_HOSTS = [ '*' ]
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "market/media_cdn")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"


# # Additional locations of static files
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# ]


# List of finder classes that know how to find static files in
# various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

# List of callables that know how to import templates from various sources.

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
   # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'DjangoWebProject3.middleware.LoginRequiredMiddleware',
)
ROOT_URLCONF = 'DjangoWebProject3.urls'
# CORS_ORIGIN_ALLOW_ALL
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    'localhost:8000',
    'https://perfectmoney.is',
)

CORS_ORIGIN_HEADERS =(
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'user-agent',
    'x-requested-with',
    'x-csrftoken',

)
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'DjangoWebProject3.wsgi.application'

TEMPLATE_DEBUG = False


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lewicpro@gmail.com'
EMAIL_HOST_PASSWORD = 'lw191919'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'lewicpro@gmail.com'
#BROKER_URL = "amqp://guest:guest@localhost:5672//"
# CELERY_BROKER_URL = 'django://'

# #: Only add pickle to this list if your broker is secured
# #: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'django-db'
# # CELERY_RESULT_BACKEND = 'django-cache'

INSTALLED_APPS = (
    # 'django_celery_beat',
    # "django_celery_results",
    'timedcontent',
    'representatives',
    'crispy_forms',
    'django_pesapal',
    'cryptoreseller',
    'market',
    'app',
    # 'sorl.thumbnail',
    'corsheaders',
    'rest_framework',
    'jobs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }

# Specify the default test runner.
# TEST_RUNNER = 'django.test.runner.DiscoverRunner'
AUTH_PROFILE_MODULE = 'app.UserInfo'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
# AUTHENTICATION_BACKENDS = (
#     'app.Backend.EmailBackend',
# )

# PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'app:deposits'  # this needs to be a reversible