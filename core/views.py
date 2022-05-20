from django.shortcuts import render
from django.views import View

class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)
