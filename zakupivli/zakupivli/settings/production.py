from .base import *

DEBUG = False

print("Production: ", DEBUG)

try:
    from .local import *
except ImportError:
    pass
