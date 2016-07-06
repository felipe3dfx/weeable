import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_APPS = [
    'app',
    'user',
]

INSTALLED_APPS = PROJECT_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',

    'axes.apps.AppConfig',
    'compressor',
    'markdownx',
    'django_extensions',
    'django_jenkins',
    'raven.contrib.django.raven_compat',
    'django_countries',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
                'app.context_processors.analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

AUTH_USER_MODEL = 'user.User'

VALIDATOR_PATH = 'django.contrib.auth.password_validation.{0}'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': VALIDATOR_PATH.format('UserAttributeSimilarityValidator'),
    },
    {
        'NAME': VALIDATOR_PATH.format('MinimumLengthValidator'),
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': VALIDATOR_PATH.format('CommonPasswordValidator'),
    },
    {
        'NAME': VALIDATOR_PATH.format('NumericPasswordValidator'),
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en-us'

SEARCH_LANGS = {
    'es-co': 'spanish',
    'en-us': 'english',
}

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/uploads/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

DEFAULT_FROM_EMAIL = 'info@weeable.com'

LOGIN_REDIRECT_URL = 'user:user_form'

LOGIN_URL = 'auth_login'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# django-axes
AXES_LOGIN_FAILURE_LIMIT = 3
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = 24
AXES_LOCKOUT_TEMPLATE = '429.html'

# django-compressor
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]

# django-markdownx
MARKDOWNX_MARKDOWNIFY_FUNCTION = 'markdownx.utils.markdownify'
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.smart_strong',
    'markdown.extensions.nl2br',
    'markdown.extensions.sane_lists',
    'markdown.extensions.smarty',
]
MARKDOWNX_URLS_PATH = '/markdownx/markdownify/'
MARKDOWNX_UPLOAD_URLS_PATH = '/markdownx/upload/'
MARKDOWNX_MEDIA_PATH = 'markdownx/'
MARKDOWNX_UPLOAD_MAX_SIZE = 2097152     # 2MB - maximum file size
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png']
MARKDOWNX_IMAGE_MAX_SIZE = {'size': (800, 0), 'quality': 90}
MARKDOWNX_EDITOR_RESIZABLE = True

# django-registration
ACCOUNT_ACTIVATION_DAYS = 3

# pylint: disable=wrong-import-position,unused-wildcard-import,wildcard-import
if any(x in sys.argv for x in ('test', 'jenkins')):
    from app.test_settings import *
else:
    from app.local_settings import *     # pylint: disable=E0611,E0401
