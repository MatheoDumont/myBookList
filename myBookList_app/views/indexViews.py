from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from myBookList_app.forms.CustomUserCreationForm import CustomUserCreationForm


def index(request):

    authform = AuthenticationForm()
    creationUserForm = CustomUserCreationForm()

    return render(request, 'index/index.html', {
        'authForm': authform,
        'createForm': creationUserForm
    })
