from django.db.models import Q
from django.http import JsonResponse
from django.views import View

from myBookList_app.services.ApiServices import search_author


class ApiAuthor(View):
    sessionAuthorBookKey = 'book_creation_author_id'

    def get(self, request):
        if not request.GET['q']:
            return JsonResponse(None)

        # On récupère la requête avec dedans l'author recherché
        q = request.GET['q']

        # Algo de recherche
        authorslist = search_author(q)

        return JsonResponse(authorslist, safe=False)
