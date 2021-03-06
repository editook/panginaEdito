#instancias del proyecto con que valores inicializa
import os
from unipath import Path
# instalado pip install unipath
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#3 = niveles de carpeta
SECRET_KEY = 'efa%6h^^p#x&uw5!u^3+-7+hp9rlje0udc$pj(#u7g%9*=k#*5'

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TERCEROS = [

]

LOCAL = [
    'modelo.logicanegocio',
    'apps.home',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL

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

WSGI_APPLICATION = 'PaginaEdito.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES_DIRS = [Path(__file__).ancestor(3).child('templates')]
#archivos html alojados