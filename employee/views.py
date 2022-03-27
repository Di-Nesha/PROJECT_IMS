from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.
def employee_list(request):
        return render(request,"employee/employee_list.html")

#Insert & Update Functions
def employee_form(request):
        form = EmployeeForm()
        return render(request,"employee/employee_form.html",{'form':form})

#Delete Function
def employee_delete(request):
        return        