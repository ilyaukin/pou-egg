"""
Django settings for pou project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from configurations import Configuration


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
class Dev(Base):
    BASE_DIR = Base.BASE_DIR

    SECRET_KEY = '+3)zodgcj)8sp!r=wm)h()@_hpg5%*eb!kvamh76%9e=3_e1l('

    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'egg',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'pou.urls'

    WSGI_APPLICATION = 'pou.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )


class Production(Dev):
    DEBUG = False

    ALLOWED_HOSTS = ['.pythonanywhere.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'kzerby.mysql.pythonanywhere-services.com',
            'NAME': 'kzerby$egg',
            'USER': 'kzerby',
            'PASSWORD': os.environ.get('EGG_SECRET', ''),
        }
    }
