from django.contrib.auth.models import User
from django.db import models

from .services.BookServices import generate_path_for_save
# à compléter
choicesNationality = ("FR", "France"), ("US", "USA"), ("UK", "United Kingdom"), ("Ru", "Russie"), ("Ge", "Allemagne"), ("Au", "Autriche")

choicesType = ("tri", "trilogie"), ("cyc", "cycle"), ("sin", "single")

stateUserBook = ("toRead", "à Lire"), ("abandoned", "abandonné"), ("pending", "en Attente"), ("onGoing", "en Cours"), ("undefined", "Non défini")


# ------------------------------  Models  --------------------------------------


class Author(models.Model):
    name = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    birthDay = models.DateField()
    deathDay = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=choicesNationality, max_length=100)
    genres = models.ManyToManyField(to='Genre', db_table='Link_Author_To_Genre')

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name + " " + self.forename


# -----------------------------------------------------------------------------


class Book(models.Model):
    """
    On nomme la table jointure Book-Genre : 'Book_Link_Genre'
    """
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(to="Genre", db_table='Link_Book_To_Genre')
    synopsis = models.TextField(blank=True)
    isbn = models.CharField(blank=True, max_length=100)
    front_page_cover = models.ImageField(default=None,
                                         upload_to=generate_path_for_save,
                                         max_length=1000
                                         )

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    def __str__(self):
        return self.name


# -----------------------------------------------------------------------------


class Serie(models.Model):
    type = models.CharField(choices=choicesType, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    books = models.ManyToManyField(Book, through="SerieBook")

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.name


# -----------------------------------------------------------------------------


class SerieBook(models.Model):
    # NOTE This model make the link between books and their series

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    num = models.IntegerField()

    class Meta:
        verbose_name = "SerieBook"
        verbose_name_plural = "SerieBooks"

    def __str__(self):
        return self.serie.name + " | tome " + str(self.num) + " : " + self.book.name


# -----------------------------------------------------------------------------

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(to='Genre', db_table='Link_Profil_To_Genre')

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return self.user.get_full_name()


# -----------------------------------------------------------------------------


class UserBook(models.Model):
    """
    Le timestamp représente le timestamp de la dernière modification de 'state'
    """
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    state = models.CharField(choices=stateUserBook, max_length=100)
    note = models.IntegerField()
    comment = models.CharField(max_length=1000)
    readTimes = models.IntegerField()

    def __str__(self):
        return self.profil.__str__() + " " + self.book.__str__()


# ------------------------------------------------------------------------------


class Genre(models.Model):
    """
    Genre Littéraire
    name = nom
    numberAuthor : correspond au nombre d'author de cette catégorie
    numberBook : correspond au nombre de livre "    "   "   "
    """
    name = models.CharField(max_length=100)
    numberBook = models.PositiveIntegerField(default=0)
    numberAuthor = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
