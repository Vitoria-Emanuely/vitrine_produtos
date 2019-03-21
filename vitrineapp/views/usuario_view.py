from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View

from vitrineapp.forms import UsuarioForm
from vitrineapp.models import UsuarioModel


class CadastroUsuarioView(View):
    template = 'cadastro_usuario.html'

    def get(self, request):
        form = UsuarioForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = UsuarioModel.objects.latest('id')
            usuario.groups.add(Group.objects.get(pk=1))
            usuario.save()
            return redirect('vitrine:index')
        return render(request, self.template, {'form': form})
