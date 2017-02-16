import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Can not find environment variable: %s" % var_name
        raise ImproperlyConfigured(error_msg)
