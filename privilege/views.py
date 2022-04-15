from django.shortcuts import render,redirect
from .forms import PrivilegeForm
from .models import Privilege

#Create your views here.
def privilege_list(request):
        context = {'privilege_list':Privilege.objects.all()}
        return render(request,"privilege/privilege_list.html",context)

# Insert & Update Function
def privilege_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = PrivilegeForm()
                else:
                        privilege = Privilege.objects.get(pk=id)
                        form = PrivilegeForm(instance=privilege)
                return render(request,"privilege/privilege_form.html",{'form':form})
        else:
                if id==0:
                        form = PrivilegeForm(request.POST)
                else:
                        privilege = Privilege.objects.get(pk=id)
                        form = PrivilegeForm(request.POST,instance=privilege)
                if form.is_valid():
                        form.save()
                return redirect('/privilege/list')

#Delete Function
def privilege_delete(request,id):
        privilege = Privilege.objects.get(pk=id)
        privilege.delete()
        return redirect('/privilege/list')