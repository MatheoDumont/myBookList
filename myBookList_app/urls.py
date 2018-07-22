from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexViews.index, name='index'),
]
