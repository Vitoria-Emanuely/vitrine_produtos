from django import forms
from django.forms import ModelForm

from vitrineapp.models import CategoriaModel, ProdutoModel


class ProdutoForm(ModelForm):
    nome_produto = forms.CharField(max_length=100)
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