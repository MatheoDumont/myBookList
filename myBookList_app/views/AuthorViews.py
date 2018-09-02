from django.shortcuts import render, redirect
from django.views import View

from myBookList_app.forms.AuthorForms import AuthorForm


class Create(View):
    template = 'author/create.html'

    def get(self, request):
        form = AuthorForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

        return render(request, self.template, {'form': form})
