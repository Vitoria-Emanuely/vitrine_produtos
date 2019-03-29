from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from vitrineapp.forms import CategoriaForm


class CadastroCateView(View):
    template = 'cadastro_cate.html'

    def get(self, request):
        form = CategoriaForm
        if not request.user.is_authenticated:
            HttpResponseRedirect('')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vitrine:cadastro_produto')
        return render(request, self.template, {'form': form})