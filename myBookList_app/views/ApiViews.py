from django.db.models import Q
from django.http import JsonResponse
from django.views import View

from myBookList_app.models import Author


class ApiAuthor(View):
    sessionAuthorBookKey = 'book_creation_author_id'

    def get(self, request):
        if not request.GET['q']:
            return JsonResponse(None)

        # On récupère la requête avec dedans l'author recherché
        q = request.GET['q']

        # Il serait intéressant de généraliser cet algorithme pour pouvoir l'utiliser ailleur si besoin

        # Vérifier si il y a plus de 1 mot si oui, faire la recherche en comptant le premier mot
        # comme le prénom puis le second comme le nom et faire la recherche adaptée

        # Comme mécanisme pour être sûr d'être le plus éxhaustif, faire la recherche ci-dessous et croiser les
        # résultats obtenus ci-dessus pour maximiser les chances de trouver l'auteur rechercher
        authors_qd = Author.objects.filter(Q(name__contains=q) | Q(forename__contains=q))

        print(authors_qd)

        # On écrit dans le dict pour pouvoir récuperer l'author après dans le book/create/post en autre
        if self.sessionAuthorBookKey not in request.session:
            request.session[self.sessionAuthorBookKey] = dict()
        else:
            for author in authors_qd:
                request.session[self.sessionAuthorBookKey][author.name + " " + author.forename] = author.id

        # On garde seulement les valeurs 'id', 'name' et 'forename'
        authors_qd = authors_qd.values('id', 'name', 'forename')

        # On transforme le QueryDict en liste
        authorslist = [author for author in authors_qd]
        print(authorslist)

        return JsonResponse(authorslist, safe=False)

    @property
    def getSessionAuthorBookKey(self):
        return self.sessionAuthorBookKey
