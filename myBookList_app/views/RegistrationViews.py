from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.views import View

from myBookList_app.forms.RegistrationForms import CustomUserCreationForm


class SignIn(View):
    template = 'registration/sign-in.html'

    def get(self, request):
        form = CustomUserCreationForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

        return render(request, self.template, {'form': form})


class LogIn(View):
    template = 'registration/login.html'
    next = None

    def get(self, request):
        form = AuthenticationForm(label_suffix='')

        if request.GET['next']:
            request.session['next'] = request.GET['next']

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            data = form.clean()
            user = form.get_user()
            login(request, user)

            if 'next' in request.session:
                return redirect(resolve(request.session['next']).url_name)

            return redirect(reverse('index'))

        return render(request, self.template, {'form': form})


class LogOut(View):
    template = 'registration/logout.html'

    def get(self, request):

        if request.user.is_authenticated:
            logout(request)

            return render(request, self.template, {'was_connected': True})

        else:
            return render(request, self.template, {'was_connected': False})





















