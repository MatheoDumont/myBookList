from ..models import Book
from django.forms import ModelForm
from django import forms


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'date', 'synopsis', 'isbn', 'author', 'genres', 'front_page_cover')

        labels = {
            'name': 'Nom',
            'date': 'Date',
            'synopsis': 'Synopsis',
            'isbn': 'ISBN',
            'author': 'Auteur',
            'genres': 'Genre littéraire',
            'front_page_cover': 'Page de Couverture'
        }

        help_texts = {
            'genres': 'Vous pouvez en séléctionner plusieurs en maintenant CTRL+click',
            'author': "Entrer l'Auteur au format 'Prénom Nom' facilitera la recherche !"
        }

        widgets = {
            'date': forms.DateInput(),
            'author': forms.TextInput()
        }
