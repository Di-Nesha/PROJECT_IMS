from hashlib import new
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import New

#Create your views here.
def employee_list(request):
        context = {'employee_list':New.objects.all()}
        return render(request,"employee/employee_list.html",context)

# Insert & Update Function
def employee_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = EmployeeForm()
                else:
                        employee = New.objects.get(pk=id)
                        form = EmployeeForm(instance=employee)
                return render(request,"employee/employee_form.html",{'form':form})
        else:
                if id==0:
                        form = EmployeeForm(request.POST)
                else:
                        employee = New.objects.get(pk=id)
                        form = EmployeeForm(request.POST,instance=employee)
                if form.is_valid():
                        form.save()
                return redirect('/employee/list')

#Delete Function
def employee_delete(request,id):
        employee = New.objects.get(pk=id)
        employee.delete()
        return redirect('/employee/list')