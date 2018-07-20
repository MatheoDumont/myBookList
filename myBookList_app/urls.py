from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.IndexViews.Index.as_view(), name='index'),
    path('registration/sign-in', views.RegistrationViews.SignIn.as_view(), name='Registration sign-in'),
    path('registration/login', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                            redirect_field_name='index'),
         name='Registration login'),
]
