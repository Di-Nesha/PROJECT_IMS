from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User

#Create your views here.

def user_list(request):
        return render(request,"user/user_list.html")

def user_form(request):
        return

def user_delete(request):
        return


# def user_list(request):
#         context = {'user_list':User.objects.all()}
#         return render(request,"user/user_list.html",context)

# # Insert & Update Function
# def user_form(request, id=0):
#         if request.method == "GET":
#                 if id==0:
#                         form = UserForm()
#                 else:
#                         user = User.objects.get(pk=id)
#                         form = UserForm(instance=user)
#                 return render(request,"user/user_form.html",{'form':form})
#         else:
#                 if id==0:
#                         form = UserForm(request.POST)
#                 else:
#                         user = User.objects.get(pk=id)
#                         form = UserForm(request.POST,instance=user)
#                 if form.is_valid():
#                         form.save()
#                 return redirect('/user/list')

# #Delete Function
# def user_delete(request,id):
#         user = User.objects.get(pk=id)
#         user.delete()
#         return redirect('/user/list')