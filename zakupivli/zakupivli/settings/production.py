from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "csh99bu%s9t&zwpcz*%y@bdp8gpbkn$as3+5#csh99bu%s9t&zwpcz*%y@bdp82b06%!7yu0fsg"

DEBUG = False

print("Production: ", DEBUG)

try:
    from .local import *
except ImportError:
    pass
