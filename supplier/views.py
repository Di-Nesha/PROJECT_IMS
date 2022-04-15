from django.shortcuts import render,redirect
from .forms import SupplierForm
from .models import Supplier

#Create your views here.
def supplier_list(request):
        context = {'supplier_list':Supplier.objects.all()}
        return render(request,"supplier/supplier_list.html",context)

# Insert & Update Function
def supplier_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = SupplierForm()
                else:
                        supplier = Supplier.objects.get(pk=id)
                        form = SupplierForm(instance=supplier)
                return render(request,"supplier/supplier_form.html",{'form':form})
        else:
                if id==0:
                        form = SupplierForm(request.POST)
                else:
                        supplier = Supplier.objects.get(pk=id)
                        form = SupplierForm(request.POST,instance=supplier)
                if form.is_valid():
                        form.save()
                return redirect('/supplier/list')

#Delete Function
def supplier_delete(request,id):
        supplier = Supplier.objects.get(pk=id)
        supplier.delete()
        return redirect('/supplier/list')