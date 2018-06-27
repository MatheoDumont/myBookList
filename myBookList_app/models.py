from django.db import models

# à compléter
choicesNationality = ("FR", "France"), ("US", "USA"), ("UK", "United Kingdom")

choicesType = ("tri", "trilogie"), ("cyc", "cyle")

# ------------------------------  Models --------------------------------------


class Author(models.Model):
    name = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    birthDay = models.DateField()
    deathDay = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=choicesNationality, max_length=100)
    listeGenres = list()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name + " " + self.forename

# -----------------------------------------------------------------------------


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    listGenres = list()
    synopsis = models.TextField(blank=True)
    isbn = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

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
    # NOTE This model make the link between books and their serie

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    num = models.IntegerField()

    class Meta:
        verbose_name = "SerieBook"
        verbose_name_plural = "SerieBooks"

    def __str__(self):
        return self.serie.name + " | tome " + str(self.num) + " : " + self.book.name
