from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class IndexView(View):
    template = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/lista_produtos')
        return render(request, self.template)