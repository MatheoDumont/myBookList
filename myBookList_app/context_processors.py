"""
Variable de context ajoutés à chaque chargement de page.
On indique à django l'utilisation de ce fichier en l'ajoutant dans:
    settings.Templates.options.context_processors : myBookList_app.context.processors.skeleton_context

Un context_processor doit obligatoirement retourner un dict.
Chaque context_processor reçcoit une instance de HttpRequest.
Pour plus d'infos : https://docs.djangoproject.com/fr/2.1/ref/templates/api/#django.template.RequestContext
"""


def skeleton_context(request):
    return dict()
