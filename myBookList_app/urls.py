from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from myBookList import settings
from myBookList_app.views import IndexViews, RegistrationViews, BookViews, AuthorViews, SearchViews
from .views import *

urlpatterns = [
    path('', IndexViews.Index.as_view(), name='index'),

    path('registration/sign-in', RegistrationViews.SignIn.as_view(), name='Registration sign-in'),
    path('registration/login', RegistrationViews.LogIn.as_view(), name='Registration login'),
    path('registration/logout', RegistrationViews.LogOut.as_view(), name='Registration logout'),

    path('book/create', BookViews.Create.as_view(), name='Book create'),

    path('author/create', AuthorViews.Create.as_view(), name='Author create'),
    path('author/api', AuthorViews.Api.as_view(), name='Author api'),

    path('search/', SearchViews.Search.as_view(), name='Search')

]
