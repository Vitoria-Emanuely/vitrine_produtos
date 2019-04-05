from django.db import models
from django.db.models import Model


class ComentarioModel(Model):
    produto = models.ForeignKey('vitrineapp.ProdutoModel', on_delete=models.CASCADE, related_name='comentarios')
    # usuario = models.ForeignKey('vitrineapp.UsuarioModel', on_delete=models.CASCADE)
    texto = models.TextField()

    def __unicode__(self):
        return self.texto

    def __str__(self):
        return self.texto
