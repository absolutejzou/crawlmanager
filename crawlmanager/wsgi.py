"""
WSGI config for crawlmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    mode = os.environ['SERVER_MODE']
    settings = 'crawlmanager.settings.{}'.format(mode)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
except KeyError:
    raise KeyError("Couldn't get SERVER_MODE from environment variable. "
                  "Please make sure you have set the environment variable "
                  "successfully!")


application = get_wsgi_application()
