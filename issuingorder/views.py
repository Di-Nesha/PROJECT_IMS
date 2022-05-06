from django.shortcuts import render,redirect
from .forms import IssuingOrderForm
from .models import IssuingOrder

#Create your views here.
def issuingorder_list(request):
        context = {'issuingorder_list':IssuingOrder.objects.all()}
        return render(request,"issuingorder/issuingorder_list.html",context)

# Insert & Update Function
def issuingorder_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = IssuingOrderForm()
                else:
                        issuingorder = IssuingOrder.objects.get(pk=id)
                        form = IssuingOrderForm(instance=issuingorder)
                return render(request,"issuingorder/issuingorder_form.html",{'form':form})
        else:
                if id==0:
                        form = IssuingOrderForm(request.POST)
                else:
                        issuingorder = IssuingOrder.objects.get(pk=id)
                        form = IssuingOrderForm(request.POST,instance=issuingorder)
                if form.is_valid():
                        form.save()
                return redirect('/issuingorder/list')

#Delete Function
def issuingorder_delete(request,id):
        issuingorder = IssuingOrder.objects.get(pk=id)
        issuingorder.delete()
        return redirect('/issuingorder/list')