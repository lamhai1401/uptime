"""
Dev config setting
"""
from configs.base import *  # pylint: disable=W0401,W0614 # NOQA

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]  # NOQA
