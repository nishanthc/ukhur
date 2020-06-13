from .base import *
import environ

DEBUG = True
ALLOWED_HOSTS = ['*']
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading local.env file

environ.Env.read_env(env_file=os.path.join(
    BASE_DIR, "settings", "local.env"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}
