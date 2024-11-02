from pathlib import Path

from environ import Env
env=Env()
Env.read_env()

ENVIRONMENT = env('ENVIRONMENT',default="production")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*','https://djangoauth20241102.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://djangoauth20241102.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    "widget_tweaks",
    "slippers",
]

ALLAUTH_UI_THEME = "light"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates',BASE_DIR/'components'],
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

WSGI_APPLICATION = 'src.wsgi.application'

import dj_database_url

if ENVIRONMENT == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    }


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

LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT=BASE_DIR /'staticfiles'

MEDIA_URL = 'media/'

if ENVIRONMENT == 'development':
    MEDIA_ROOT = BASE_DIR / 'media' 
else:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE={
        'CLOUDINARY_URL': env('CLOUDINARY_URL')
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#配置django-allauth其它選項
# 強制註冊郵箱驗證(註冊成功後，會發送一封驗證郵件，用戶必須驗證郵箱後，才能登陸)
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  

# 登錄方式(選擇用戶名或者郵箱都能登錄)
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# 設置用戶註冊的時候必須填寫郵箱地址
ACCOUNT_EMAIL_REQUIRED = True

# 用戶登出(需要確認)
ACCOUNT_LOGOUT_ON_GET = False 

# 配置郵箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_ADDRESS')

# 這個不是郵箱密碼，而是授權碼
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')

# 這裡必須是True，否則發送不成功
EMAIL_USE_TLS = True 

# 發件人
EMAIL_FROM = "ryowu0329@gmail.com" 
 
# 默認發件人(如果不添加DEFAULT_FROM_EMAIL字段可能會導致如下錯誤: 
# 451, b'Sender address format error.', 'ryowuandjanet@localhost')
DEFAULT_FROM_EMAIL = f"毛毛與秀秀的 {env('EMAIL_ADDRESS')}"
ACCOUNT_EMAIL_SUBJECT_PREFIX=''



LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': ''
        }
    },
    'github': {
        'APP': {
            'client_id': env('GITHUB_CLIENT_ID'),
            'secret': env('GITHUB_CLIENT_SECRET'),
        },
        'SCOPE': [
            'read:user',
            'user:email',
        ]
    }
}

# Slippers configuration
SLIPPERS_COMPONENT_DIRS = [
    BASE_DIR/'templates',
    BASE_DIR/'components',
]

# 確保這行存在並指向正確的位置
SLIPPERS_COMPONENTS_FILE = BASE_DIR / 'templates' / 'components.yaml'
