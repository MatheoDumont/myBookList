"""
Views pour la barre de recherche dans l'index
"""
from django.shortcuts import render, redirect
from django.views import View


from myBookList_app.services.SearchServices import search
from ..forms.SearchForms import SearchForm


class Search(View):
    template = 'search/search.html'

    def get(self, request):
        form = SearchForm(request.GET)

        if form.is_valid():

            res = search(form.cleaned_data['search'])

            return render(request, self.template, {'searchForm': form,
                                                   'res_search': res
                                                   })

        return redirect('index')
