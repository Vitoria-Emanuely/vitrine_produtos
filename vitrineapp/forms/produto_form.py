from django import forms
from django.forms import ModelForm

from vitrineapp.models import CategoriaModel, ProdutoModel, ComentarioModel


class ProdutoForm(ModelForm):
    nome_produto = forms.CharField(max_length=100)
    preco_produto = forms.DecimalField(decimal_places=2, max_digits=10000)
    descricao_produto = forms.CharField(max_length=200)
    id_categoria = forms.ModelChoiceField(
        queryset=CategoriaModel.objects.all()
    )

    def save(self, commit=True):
        produto = super(ProdutoForm, self).save(commit=False)
        if commit:
            produto.save()

    class Meta:
        model = ProdutoModel
        exclude = ()


class ComentarioForm(ModelForm):
    class Meta:
        model = ComentarioModel
        fields = ('texto', )
