import os
import environ

# Set up the environment variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Security settings
SECRET_KEY = 'kobl@t=yw9d*0y%jt2gjnq78=u!z_rrxb&w8e47l!(jz@m79zy'
DEBUG = True
ALLOWED_HOSTS = ["localhost" , "127.0.0.1"]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'corsheaders',
    'core',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Celery settings
CELERY_BROKER_URL = env('CELERY_BROKER_URL')  # Redis broker URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Optional: Using Celery Beat for periodic tasks
INSTALLED_APPS += ['django_celery_beat']


# CORS settings
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ('DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT')
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Origin',
    'sentry-trace'
)
# CORS_ORIGIN_WHITELIST = [
#     "*"
# ]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('MONGO_DB_NAME'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': env('MONGO_HOST'),
            'port': int(env('MONGO_PORT')),
            'username': env('MONGO_USER'),
            'password': env('MONGO_PASSWORD'),
            'authSource': 'admin',  # Adjust as per your MongoDB setup
            'authMechanism': 'SCRAM-SHA-256',  # Ensure this matches your MongoDB configuration
        }
    }
}

# Stripe keys (replace with actual keys)
STRIPE_PUBLIC_KEY = 'STRIPE_TEST_PUBLIC_KEY'
STRIPE_SECRET_KEY = 'STRIPE_TEST_SECRET_KEY'

# URL configuration
ROOT_URLCONF = 'djecommerce.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


#allauth
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = False 

ACCOUNT_AUTHENTICATION_METHOD = "username"

# WSGI application
WSGI_APPLICATION = 'djecommerce.wsgi.application'

# Language and timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_root'),
    '/var/www/static/',
]

# Authentication settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# Crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'


