# Django settings for test_project project.
from __future__ import print_function
import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'dev.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/' # Set this so our files can use /media/

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v!y*k!pa947m205&g*ih*a20651l=-gagc_$ntdjt9$_g85c=!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',

)

ROOT_URLCONF = 'test_project.urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"), )

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "test_project.fun",
    'django_wysiwyg'
)

DJANGO_WYSIWYG_FLAVOR = 'yui'       # Default
# DJANGO_WYSIWYG_FLAVOR = 'ckeditor'  # Requires you to also place the ckeditor files here:
# NOTE: If you are using DJANGO 1.3, you will want to follow the docs and use
# STATIC_URL instead of MEDIA_URL here.
# DJANGO_WYSIWYG_MEDIA_URL = "%s/ckeditor" % MEDIA_URL


# Support newer Django versions:
import django
if django.VERSION >= (1,3):
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
    STATIC_URL = '/static/'

    ADMIN_MEDIA_PREFIX = '/static/admin/'

    INSTALLED_APPS += (
        "django.contrib.staticfiles",
    )

    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.' + DATABASE_ENGINE,
            'NAME':     DATABASE_NAME,
            'USER':     DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST':     DATABASE_HOST,
            'PORT':     DATABASE_PORT,
        },
    }


# Auto configure resources for editor flavors:
if 'tinymce' in DJANGO_WYSIWYG_FLAVOR:
    print("NOTE: Adding 'tinymce' to INSTALLED_APPS")
    INSTALLED_APPS += (
        'tinymce',
    )
elif 'ckeditor' in DJANGO_WYSIWYG_FLAVOR:
    print("NOTE: Adding 'ckeditor' to INSTALLED_APPS")
    INSTALLED_APPS += (
        'ckeditor',
    )
    CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

