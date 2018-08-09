from ..models import Book
from django.forms import ModelForm
from django import forms


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'date', 'synopsis', 'isbn', 'author', 'genres')

        labels = {
            'name': 'Nom',
            'date': 'Date',
            'synopsis': 'Synopsis',
            'isbn': 'ISBN',
            'author': 'Auteur',
            'genres': 'Genre littéraire'
        }

        help_texts = {
            'genres': 'Vous pouvez en séléctionner plusieurs en maintenant CTRL+click',
        }

        widgets = {
            'date': forms.DateInput(),
            # 'author': forms.TextInput()
        }
