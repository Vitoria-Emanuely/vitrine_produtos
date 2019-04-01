from django.db import models
from django.db.models import Model


class CategoriaModel(Model):
    desc_categoria = models.TextField(max_length=100)

    def __unicode__(self):
        return self.desc_categoria

    def __str__(self):
        return self.desc_categoria
