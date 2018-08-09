from django.shortcuts import render
from . import IndexViews


def get_user(request):

    if request.user.is_authenticated:
        return request.user
    else:
        return False


def cut_in_two(form):
    """
    return un tuple de field d'un form coupé en deux pour faciliter l'affichage d'un form en deux colonnes
    :param form:
    :return tuple:
    """
    visible_field = form.visible_fields()
    size = len(visible_field)

    premPartie = visible_field[0: size//2]
    secPartie = visible_field[size//2: size]

    return premPartie, secPartie
