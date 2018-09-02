from django.urls import path
from django.contrib.auth import views as auth_views

from myBookList_app.views import ApiViews, IndexViews, RegistrationViews, BookViews, AuthorViews
from .views import *

urlpatterns = [
    path('', IndexViews.Index.as_view(), name='index'),

    path('registration/sign-in', RegistrationViews.SignIn.as_view(), name='Registration sign-in'),
    path('registration/login', RegistrationViews.LogIn.as_view(), name='Registration login'),
    path('registration/logout', RegistrationViews.LogOut.as_view(), name='Registration logout'),

    path('book/create', BookViews.Create.as_view(), name='Book create'),

    path('author/create', AuthorViews.Create.as_view(), name='Author create'),

    path('api/author', ApiViews.ApiAuthor.as_view(), name='Api author'),
]
