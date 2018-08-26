from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from myBookList_app.services.BookServices import build_post
from ..forms.BookForms import *
from django.shortcuts import *

"""
infos = https://docs.djangoproject.com/fr/2.0/topics/http/file-uploads/
Pour gérer les fichiers
"""


@method_decorator(login_required, name="dispatch")
class Create(View):
    template = 'book/create.html'

    def get(self, request):
        form = BookForm()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        # On build le post en remplacant les données necéssaires
        request.POST = build_post(request)

        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, self.template, {
            'form': form,
        })


class Read(View):
    template = ''

    def get(self, request):
        pass


class Update(View):
    template = ''

    def get(self, request):
        pass

    def post(self, request):
        pass
