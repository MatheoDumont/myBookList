from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.IndexViews.Index.as_view(), name='index'),

    path('registration/sign-in', views.RegistrationViews.SignIn.as_view(), name='Registration sign-in'),
    path('registration/login', views.RegistrationViews.LogIn.as_view(), name='Registration login'),
    path('registration/logout', views.RegistrationViews.LogOut.as_view(), name='Registration logout'),

    path('book/create', views.BookView.Create.as_view(), name='Book create'),
]
