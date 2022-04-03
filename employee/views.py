from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import New

#Create your views here.
def employee_list(request):
        context = {'employee_list':New.objects.all()}
        return render(request,"employee/employee_list.html",context)

# Insert & Update Function
def employee_form(request):
        if request.method == "GET":
                form = EmployeeForm()
                return render(request,"employee/employee_form.html",{'form':form})
        else:
                form = EmployeeForm(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('/employee/list')

#Delete Function
def employee_delete(request):
        return