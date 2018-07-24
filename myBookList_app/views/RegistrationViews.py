from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from myBookList_app.forms.registrationForms import CustomUserCreationForm
from myBookList_app.views.Shortcut import render_with_skelet


class SignIn(View):
    template = 'registration/sign-in.html'

    def get(self, request):
        form = CustomUserCreationForm()

        return render_with_skelet(request, self.template, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

        return render_with_skelet(request, self.template, {'form': form})


class LogIn(View):
    template = 'registration/login.html'

    def get(self, request):
        form = AuthenticationForm()

        return render_with_skelet(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)

        print(request.POST)
        print(form.is_bound)
        print(form.errors)

        if form.is_valid():
            data = form.clean()
            user = form.get_user()
            login(request, user)

            return redirect(reverse('index'))

        return render_with_skelet(request, self.template, {'form': form})


class LogOut(View):
    template = 'registration/logout.html'

    def get(self, request):

        if request.user.is_authenticated:
            logout(request)

            return render_with_skelet(request, self.template, {'was_connected': True})

        else:
            return render_with_skelet(request, self.template, {'was_connected': False})





















