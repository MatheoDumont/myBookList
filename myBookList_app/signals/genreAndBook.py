from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver

from myBookList_app.models import Book

__all__ = [
    'm2mAdd_on_Genre_from_Book', 'delete_book'
]


@receiver(m2m_changed, sender=Book.genres.through, weak=False)
def m2mAdd_on_Genre_from_Book(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    """
    On incrémente numberBook du Genre lié à au Book crée de 1
    """

    if action == "post_add":
        genres = instance.genres.all()

        if genres is not None:

            for genre in genres:
                genre.numberBook += 1
                genre.save()


@receiver(pre_delete, sender=Book, weak=False)
def delete_book(sender, instance, using, **kwargs):
    """
    On decrémente numberBook du Genre lié à au Book supprimé de 1
    """

    genres = instance.genres.all()

    if genres is not None:

        for genre in genres:
            genre.numberBook -= 1
            genre.save()
