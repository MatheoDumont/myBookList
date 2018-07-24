from django.shortcuts import render
from . import IndexViews


def get_user(request):

    if request.user.is_authenticated:
        return request.user
    else:
        return False


def render_with_skelet(request, template, option=None):
    """
    USE INSTEAD OF RENDER
    Shortcut pour éviter d'appeler dans chaque render IndexViews.loadDataForIndex()

    On charge le skeleton avec les data de loadDataForIndex

    :param request:
    :param template:
    :param option:
    :return:
    """
    return render(request, template, IndexViews.loadDataForIndex(request, option))
