from django.contrib.auth.models import User


class UsuarioModel(User):
    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name