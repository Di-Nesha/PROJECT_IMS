from django.shortcuts import render,redirect
from .forms import QuotationForm
from .models import Quotation

#Create your views here.
def quotation_list(request):
        context = {'quotation_list':Quotation.objects.all()}
        return render(request,"quotation/quotation_list.html",context)

# Insert & Update Function
def quotation_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = QuotationForm()
                else:
                        quotation = Quotation.objects.get(pk=id)
                        form = QuotationForm(instance=quotation)
                return render(request,"quotation/quotation_form.html",{'form':form})
        else:
                if id==0:
                        form = QuotationForm(request.POST)
                else:
                        quotation = Quotation.objects.get(pk=id)
                        form = QuotationForm(request.POST,instance=quotation)
                if form.is_valid():
                        form.save()
                return redirect('/quotation/list')

#Delete Function
def quotation_delete(request,id):
        quotation = Quotation.objects.get(pk=id)
        quotation.delete()
        return redirect('/quotation/list')