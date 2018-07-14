from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

from myBookList_app.forms.inscriptionForms import CustomUserCreationForm


class Index(View):
    template = 'index/index.html'

    def get(self, request):
        authform = AuthenticationForm()

        return render(request, self.template, {
            'authForm': authform,
        })