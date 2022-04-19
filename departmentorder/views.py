from django.shortcuts import render,redirect
from .forms import DepartmentOrderForm
from .models import DepartmentOrder

#Create your views here.
def departmentorder_list(request):
        context = {'departmentorder_list':DepartmentOrder.objects.all()}
        return render(request,"departmentorder/departmentorder_list.html",context)

# Insert & Update Function
def departmentorder_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = DepartmentOrderForm()
                else:
                        departmentorder = DepartmentOrder.objects.get(pk=id)
                        form = DepartmentOrderForm(instance=departmentorder)
                return render(request,"departmentorder/departmentorder_form.html",{'form':form})
        else:
                if id==0:
                        form = DepartmentOrderForm(request.POST)
                else:
                        departmentorder = DepartmentOrder.objects.get(pk=id)
                        form = DepartmentOrderForm(request.POST,instance=departmentorder)
                if form.is_valid():
                        form.save()
                return redirect('/departmentorder/list')

#Delete Function
def departmentorder_delete(request,id):
        departmentorder = DepartmentOrder.objects.get(pk=id)
        departmentorder.delete()
        return redirect('/departmentorder/list')