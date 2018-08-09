from django.views import View
from ..forms.BookForms import *
from django.shortcuts import *
from ..models import *


class Create(View):
    template = 'book/create.html'

    def get(self, request):
        form = BookForm()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        b1 = Book.objects.get(id=5)

        g1 = Genre.objects.get(id=1)


        b1.genres.add(g1)
        return redirect('index')

        """
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, self.template, {
            'form': form,
        })
        :param request:
        :return:
        """


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
