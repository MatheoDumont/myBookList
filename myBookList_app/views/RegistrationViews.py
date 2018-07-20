from pprint import pprint

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from myBookList_app.forms.registrationForms import CustomUserCreationForm


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

