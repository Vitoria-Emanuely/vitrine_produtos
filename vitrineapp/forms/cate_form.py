from django import forms
from django.forms import ModelForm

from vitrineapp.models import CategoriaModel


class CategoriaForm(ModelForm):
    desc_categoria = forms.CharField(max_length=100)

    def save(self, commit=True):
        categoria = super(CategoriaForm, self).save(commit=False)
        if commit:
            categoria.save()

    class Meta:
        model = CategoriaModel
        exclude = ()

