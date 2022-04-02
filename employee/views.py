from email.headerregistry import HeaderRegistry
from django.shortcuts import render

#Create your views here.

def employee_list(request):
        return render(request,"employee/employee_list.html")

# Insert & Update Function
def employee_form(request):
        return render(request,"employee/employee_form.html")

#Delete Function
def employee_delete(request):
        return