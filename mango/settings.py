"""
Django settings for mango project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
HOME_DIR = os.path.expanduser('~')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(HOME_DIR, '.secrets/django.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MAINTENANCE_MODE = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'resume',
    'contact',
    'blog',
    'portfolio',
    'martor',
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

ROOT_URL = '/'
ROOT_URLCONF = 'mango.urls'

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
                'mango.context_processors.project_context',
                'mango.context_processors.root_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'mango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'media',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'files/staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'files/mediafiles'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Contact
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'contact@<your-domain>.com'
EMAIL_HOST = '<Email Host SMTP Address>'
EMAIL_HOST_USER = '<Username>'
EMAIL_HOST_PASSWORD = '<Password>'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Martor
# Choices are: "semantic", "bootstrap"
MARTOR_THEME = 'bootstrap'

# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',  # to enable/disable emoji icons.
    'imgur': 'false',  # to enable/disable imgur/custom uploader.
    'mention': 'false',  # to enable/disable mention
    'jquery': 'true',  # to include/revoke jquery (require for admin default django)
    'living': 'false',  # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',  # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = True

# Imgur API Keys
# MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
# MARTOR_IMGUR_API_KEY = 'your-api-key'

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify'  # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/'  # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',  # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',  # to parse markdown mention
    'martor.extensions.emoji',  # to parse markdown emoji
    'martor.extensions.mdx_video',  # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/'  # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/'  # default

# Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'     # from webfx
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'  # default from github
MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://python.web.id/author/'  # please change this to your domain

# If you need to use your own themed "bootstrap" or "semantic ui" dependency
# replace the values with the file in your static files dir
# MARTOR_ALTERNATIVE_JS_FILE_THEME = "semantic-themed/semantic.min.js"  # default None
# MARTOR_ALTERNATIVE_CSS_FILE_THEME = "semantic-themed/semantic.min.css"  # default None
# MARTOR_ALTERNATIVE_JQUERY_JS_FILE = "jquery/dist/jquery.min.js"  # default None
