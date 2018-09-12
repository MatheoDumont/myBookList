from django import forms


class SearchForm(forms.Form):
    searchInput = forms.CharField()
