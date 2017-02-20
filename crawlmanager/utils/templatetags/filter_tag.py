from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_settings(variable_name):
    return getattr(settings, variable_name, '')
