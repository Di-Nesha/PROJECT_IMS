from django.shortcuts import render,redirect
from .forms import InventoryForm
from .models import Inventory

#Create your views here.
def inventory_list(request):
        context = {'inventory_list':Inventory.objects.all()}
        return render(request,"inventory/inventory_list.html",context)

# Insert & Update Function
def inventory_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = InventoryForm()
                else:
                        inventory = Inventory.objects.get(pk=id)
                        form = InventoryForm(instance=inventory)
                return render(request,"inventory/inventory_form.html",{'form':form})
        else:
                if id==0:
                        form = InventoryForm(request.POST)
                else:
                        inventory = Inventory.objects.get(pk=id)
                        form = InventoryForm(request.POST,instance=inventory)
                if form.is_valid():
                        form.save()
                return redirect('/inventory/list')

#Delete Function
def inventory_delete(request,id):
        inventory = Inventory.objects.get(pk=id)
        inventory.delete()
        return redirect('/inventory/list')