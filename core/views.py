from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from employee.models import New


class Password(LoginRequiredMixin, View):
    template = 'password.html'
    login_url = '/password/'
 
    def get(self, request):
        return render(request, self.template)


class Register(LoginRequiredMixin, View):
    template = 'register.html'
    login_url = '/register/'
 
    def get(self, request):
        return render(request, self.template)


class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'
 
    def get(self, request):
        return render(request, self.template)

    def get(self, request):
        news = New.objects.all()
        return render(request, self.template, {'news': news})


class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})