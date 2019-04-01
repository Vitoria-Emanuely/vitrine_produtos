from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from vitrineapp.forms import ProdutoForm
from vitrineapp.models import ProdutoModel, CategoriaModel


class ListaProdutoView(View):
    template = 'lista_produtos.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.GET = None

    def get(self, request):
        lista_produtos = ProdutoModel.objects.all()
        objeto = {
            'lista_produtos': lista_produtos
        }
        if 'q' in request.GET:
            objeto['lista_produtos'] = self.search(request.GET['q'])
        #TODO
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template, objeto)

    def search(self, query):
        if query:

            id_categoria = CategoriaModel.objects.filter(desc_categoria=query).first().id
            return {'lista_produtos':
                        ProdutoModel.objects.filter(Q(id_categoria=id_categoria))
                    }



class CadastroProdutoView(View):
    template = 'cadastro_produtos.html'

    def get(self, request):
        form = ProdutoForm
        if not request.user.is_authenticated:
            HttpResponseRedirect('')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vitrine:lista_produtos')
        return render(request, self.template, {'form': form})
