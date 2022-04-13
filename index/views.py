from django.shortcuts import render

# Create your views here.
def index_home(request):
        # context = {'index_home':New.objects.all()}
        return render(request,"index/login.html")

