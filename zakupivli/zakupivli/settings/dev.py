from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

print("development: ", DEBUG)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "csh99bu%s9t&zwpcz*%y@bdp8gpbkn$as3+5#csh99bu%s9t&zwpcz*%y@bdp82b06%!7yu0fsg"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
