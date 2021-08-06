"""
Dev config setting
"""
# pylint: disable-msg=w0614,W0401
from configs.base import *  # noqua

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]
