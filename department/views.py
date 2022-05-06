from django.shortcuts import render,redirect
from .forms import DepartmentForm
from .models import Department

#Create your views here.
def department_list(request):
        context = {'department_list':Department.objects.all()}
        return render(request,"department/department_list.html",context)

# Insert & Update Function
def department_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = DepartmentForm()
                else:
                        department = Department.objects.get(pk=id)
                        form = DepartmentForm(instance=department)
                return render(request,"department/department_form.html",{'form':form})
        else:
                if id==0:
                        form = DepartmentForm(request.POST)
                else:
                        department = Department.objects.get(pk=id)
                        form = DepartmentForm(request.POST,instance=department)
                if form.is_valid():
                        form.save()
                return redirect('/department/list')

#Delete Function
def department_delete(request,id):
        department = Department.objects.get(pk=id)
        department.delete()
        return redirect('/department/list')
        