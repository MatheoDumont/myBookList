from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexViews.Index.as_view(), name='index'),
    path('inscription/', views.SignInViews.SignIn.as_view(), name='Inscription index')
]
