# Django settings for ltt_blog project.

import os
rel_path = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

ADMINS = (
    ('Chris McDonald', 'xwraithanx@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = rel_path('media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'ltt_blog.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    rel_path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'yadba.context_processors.sidebar',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'tagging',
    'yadba',
    'south',
)

RESTRUCTUREDTEXT_FILTER_SETTINGS = {
        'doctitle_xform': False
}

try:
    from local_settings import *
except ImportError:
    import sys
    sys.stderr.write("local_settings.py could not be loaded, either does not exist or there is a syntax error.\n")
