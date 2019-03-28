from django.db import models
from django.db.models import Model


class ProdutoModel(Model):
    nome_produto = models.TextField(max_length=100)
    preco_produto = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    descricao_produto = models.TextField(max_length=200, default='  ')
    id_categoria = models.ForeignKey('CategoriaModel', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome_produto, self.preco_produto, self.descricao_produto

    def __str__(self):
        return self.nome_produto, self.preco_produto, self.descricao_produto


