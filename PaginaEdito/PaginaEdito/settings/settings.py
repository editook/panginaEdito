#instancias del proyecto con que valores inicializa
import os
from unipath import Path
from django.utils.crypto import get_random_string
# instalado pip install unipath
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#3 = niveles de carpeta

SECRET_KEY = 'efa%6h^^p#x&uw5!u^3+-7+hp9rlje0udc$pj(#u7g%9*=k#*5'

#chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
#SECRET_KEY = get_random_string(50, chars)
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modelo.logicanegocio',
]

TERCEROS = [

]

LOCAL = [
    'modelo.logicanegocio',
]

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modelo.logicanegocio',
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

ROOT_URLCONF = 'PaginaEdito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.templates.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.templates.context_processors.debug',
                'django.templates.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#archivos html alojados
#configuracion para un ambiente usado



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'Baseedu.db',
    }
}

WSGI_APPLICATION = 'PaginaEdito.wsgi.application'

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


STATIC_URL = '/static/'
