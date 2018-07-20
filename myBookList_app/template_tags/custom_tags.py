from django import template

register = template.Library()


@register.simple_tag
def format_html(value):
    return format_html(value)
