from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

"""
doc = https://docs.djangoproject.com/fr/2.0/howto/custom-template-tags/
"""

register = template.Library()


@register.simple_tag()
def build_label(label_tag, display_lab=False):
    """
    On build le label pour pouvoir le sauvegarder et proposer d'utiliser la class css 'ui label' ou non
    :param label_tag:
    :param display_lab:
    :return:
    """
    if not display_lab:
        return label_tag

    html = format_html('<div class="ui label">{}</div>', label_tag)

    return mark_safe(html)


def base_field(context, field, *args, **kwargs):
    """
    args[0] = required Boolean
    args[1] = display_label_with_class Boolean


    :param context:
    :param field:
    :param args:
    :param kwargs:
    :return:
    """
    # Champ obligatoire de base à part si spécifié False
    required = True

    # Affichage du label avec la class css 'ui label'
    display_label_with_class = False

    try:
        if args[0][0]:
            required = args[0][0]
        if args[0][1]:
            display_label_with_class = args[0][1]
    except IndexError:
        pass

    return {
        'field': field,
        'form': context['form'],
        'required': required,
        'display_label_with_class': display_label_with_class,
    }


@register.inclusion_tag('load_input/standard_field.html', takes_context=True)
def standard_field(context, field, *args, **kwargs):
    """
    A peu près tous les fields auxquels suffit ce css, à la différence de date_field ou pour afficher la date
    on veut un css spécifique à l'affichage du calendrier
    :param context:
    :param field:
    :param args:
    :return:
    """
    return base_field(context, field, args, **kwargs)


@register.inclusion_tag('load_input/date_field.html', takes_context=True)
def date_field(context, field, *args, **kwargs):
    return base_field(context, field, args, **kwargs)
