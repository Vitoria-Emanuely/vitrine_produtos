from django.db import models
from django.db.models import Model


class ProdutoModel(Model):
    nome_produto = models.TextField(max_length=100)
    id_categoria = models.ForeignKey('CategoriaModel', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome_produto

    def __str__(self):
        return self.nome_produto