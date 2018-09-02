from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from myBookList_app.models import Author


class AuthorForm(ModelForm):

    birthDate = forms.DateField(label='Date de naissance', required=False)
    deathDate = forms.DateField(label='Date de décès', required=False, help_text="Laissez vide si cet auteur n'est pas "
                                                                                "mort")

    class Meta:
        model = Author

        fields = ('name', 'forename', 'birthDate', 'deathDate', 'nationality', 'genres')

        labels = {
            'name': 'Prénom',
            'forename': 'Nom',
            'nationality': 'Nationalité',
            'genres': 'Genre littéraire',
        }

    def clean(self):
        cleaned_data = super().clean()

        birthDate = cleaned_data.get('birthDate')
        deathDate = cleaned_data.get('deathDate')

        # Pas de date de décès si date de naissance non présente
        if birthDate is None and deathDate is not None:
            self.add_error('birthDate', ValidationError(_('Il faut une date de naissance si la date de décès est présente')))

        if birthDate is not None and deathDate is not None:
            # Si la date de décès est antérieur à celle de naissance
            if deathDate < birthDate:
                self.add_error('deathDate', ValidationError(_('La date de décès ne peut pas être antérieur à celle de naissance')))










