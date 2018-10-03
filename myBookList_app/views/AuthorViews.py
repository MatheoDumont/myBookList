from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from myBookList_app.forms.AuthorForms import AuthorForm
from myBookList_app.services.AuthorServices import search_author


class Create(View):
    template = 'author/create.html'

    def get(self, request):
        form = AuthorForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

        return render(request, self.template, {'form': form})


class Api(View):
    sessionAuthorBookKey = 'book_creation_author_id'

    def get(self, request):
        if not request.GET['q']:
            return JsonResponse(None)

        # On récupère la requête avec dedans l'author recherché
        q = request.GET['q']

        # Algo de recherche d'auteur
        authorslist = search_author(q)

        return JsonResponse(authorslist, safe=False)
