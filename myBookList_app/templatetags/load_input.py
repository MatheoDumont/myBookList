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
    kwargs['required'] = required Boolean A savoir que si vous voulez avoir le choix de mettre required dans html, vous devez à l'initalisation du form le spécifié
    kwargs['display_label_css'] = Si au niveau de l'affichage on utilise la classe css label pour le label de l'input
    kwargs['display_help_text'] = Si on affichage le help_text de l'input

    exemple :
        {% standard_field form.un_field [required=True], [display_label_css=False], [display_help_text=False] %}


    """

    # Champ obligatoire par défaut
    required = True

    # Affichage du label avec la class css 'ui label'
    display_label_css = False

    # Affichage du help_text par défaut à True
    display_help_text = True

    if 'required' in kwargs:
        required = kwargs['required']

    if 'display_label_css' in kwargs:
        display_label_css = kwargs['display_label_css']

    if 'display_help_text' in kwargs:
        display_help_text = kwargs['display_help_text']

    return {
        'field': field,
        'form': context['form'],
        'required': required,
        'display_label_css': display_label_css,
        'display_help_text': display_help_text,
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
    return base_field(context, field, args, kwargs)


@register.inclusion_tag('load_input/search_field.html', takes_context=True)
def search_field(context, field, *args, **kwargs):
    return base_field(context, field, args, kwargs)


@register.inclusion_tag('load_input/non_field_error_form_field.html', takes_context=True)
def non_field_error(context, form=None, *args, **kwargs):
    retour = {
        'form': None
    }

    if form is not None:
        retour['form'] = form
    else:
        if 'form' not in context:
            raise IndexError(
                'Vous devez spécifier une instance de form pour le tag \'non_field_error\' (si vous n\'utilisez '
                'pas l\'indice par défaut \'form\', veuillez spécifier le form en arg)')
        else:
            retour['form'] = context['form']

    return retour
