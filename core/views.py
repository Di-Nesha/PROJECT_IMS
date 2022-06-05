from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from employee.models import New
from .forms import NewUserForm
from django.contrib import messages

class Register(View):
    template = 'register.html'

    def register_request(request):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("login")
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render (request=request, template_name="register", context={"form":form})

    def get(self, request):
        form = NewUserForm()
        return render(request, self.template, {'form': form})

class Password(LoginRequiredMixin, View):
    template = 'password.html'
    login_url = '/password/'
 
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

