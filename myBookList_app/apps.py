from django.apps import AppConfig


class MyBookListAppConfig(AppConfig):
    name = 'myBookList_app'

    def ready(self):
        import myBookList_app.signals
