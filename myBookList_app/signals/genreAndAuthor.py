from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver

from myBookList_app.models import Author

__all__ = [
    'm2mAdd_on_Genre_From_Author', 'delete_author'
]

@receiver(m2m_changed, sender=Author.genres.through, weak=False)
def m2mAdd_on_Genre_From_Author(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    if action == "post_add":
        genres = instance.genres.all()

        if genres is not None:

            for genre in genres:
                genre.numberAuthor += 1
                genre.save()


@receiver(pre_delete, sender=Author, weak=False)
def delete_author(sender, instance, using, **kwargs):
    genres = instance.genres.all()

    if genres is not None:

        for genre in genres:
            genre.numberAuthor -= 1
            genre.save()
