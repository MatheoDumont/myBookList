from django.views import View

from myBookList_app.views import Shortcut
from myBookList_app.views.Shortcut import render_with_skelet


class Index(View):
    template = 'index/index.html'

    def get(self, request):

        return render_with_skelet(request, self.template, None)


def loadDataForIndex(request, option=None):
    """
    Pour faciliter et centraliser le chargement des data de l'index,
    Fonction utilisée par l'index et par toutes les views
    On concatène les args de la view appelante avec les data pour l'index

    :param option: dict d'arg pour template
    :param request: request object
    :return: dict
    """

    if option is None:
        option = dict()

    data = {
        'user': Shortcut.get_user(request),
    }

    return dict(data, **option)
