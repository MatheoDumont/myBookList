from django.apps import AppConfig


class MyBookListAppConfig(AppConfig):
    name = 'myBookList_app'

    def ready(self):
        from .signals import genreAndBook,genreAndAuthor
