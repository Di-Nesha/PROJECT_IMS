from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item

#Create your views here.
def item_list(request):
        context = {'item_list':Item.objects.all()}
        return render(request,"item/item_list.html",context)

# Insert & Update Function
def item_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = ItemForm()
                else:
                        item = Item.objects.get(pk=id)
                        form = ItemForm(instance=item)
                return render(request,"item/item_form.html",{'form':form})
        else:
                if id==0:
                        form = ItemForm(request.POST)
                else:
                        item = Item.objects.get(pk=id)
                        form = ItemForm(request.POST,instance=item)
                if form.is_valid():
                        form.save()
                return redirect('/item/list')

#Delete Function
def item_delete(request,id):
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('/item/list')