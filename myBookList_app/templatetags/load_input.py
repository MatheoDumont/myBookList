from django import template
from django.template.defaulttags import *
from django.utils.safestring import SafeText

"""
doc = https://docs.djangoproject.com/fr/2.0/howto/custom-template-tags/
"""

register = template.Library()


@register.inclusion_tag('load_input/standard_field.html', takes_context=True)
def standard_field(context, field):
    return {
        'field': field,
        'form': context['form'],
    }


@register.inclusion_tag('load_input/date_field.html', takes_context=True)
def date_field(context, field):
    return {
        'field': field,
        'form': context['form'],
    }


