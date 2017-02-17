from django import template

register = template.Library()


@register.filter
def settings():
    return '1234'
