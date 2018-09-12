"""
Views pour la barre de recherche dans l'index
"""
from django.shortcuts import render
from django.views import View
from ..forms.SearchForms import SearchForm


class Search(View):
    template = 'search/search.html'

    def get(self, request):
        form = SearchForm()

        return render(request, self.template, {'form': form})



