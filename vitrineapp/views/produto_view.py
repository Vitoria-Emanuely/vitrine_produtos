from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from vitrineapp.forms import ProdutoForm
from vitrineapp.forms.produto_form import ComentarioForm
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
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template, objeto)

    def search(self, query):
        if query:
            if not CategoriaModel.objects.filter(desc_categoria=query):
                lista_produtos = ProdutoModel.objects.all()
                return lista_produtos
            id_categoria = CategoriaModel.objects.filter(desc_categoria=query).last().id
            todos_produtos = ProdutoModel.objects.filter(Q(id_categoria=id_categoria))
            return todos_produtos
        else:
            lista_produtos = ProdutoModel.objects.all()
            return lista_produtos


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


class DetalheProdutoView(View):
    template = 'detalhe_produto.html'

    def get(self, request, pk):
        produto = get_object_or_404(ProdutoModel, pk=pk)
        return render(request, self.template, {'produto': produto})

    def post(self, request, pk):
        produto = get_object_or_404(ProdutoModel, pk = pk)
        if request.method == "POST":
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.produto = produto
                produto.save()
                comentario.save()
                return redirect(reverse('vitrine:detalhe_produto', args= (produto.id, )))
        else:
            form = ComentarioForm()
        return render(request, self.template, {'form': form})
