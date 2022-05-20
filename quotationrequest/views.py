from django.shortcuts import render,redirect
from .forms import QuotationRequestForm
from .models import QuotationRequest

#Create your views here.
def quotationrequest_list(request):
        context = {'quotationrequest_list':QuotationRequest.objects.all()}
        return render(request,"quotationrequest/quotationrequest_list.html",context)

# Insert & Update Function
def quotationrequest_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = QuotationRequestForm()
                else:
                        quotationrequest = QuotationRequest.objects.get(pk=id)
                        form = QuotationRequestForm(instance=quotationrequest)
                return render(request,"quotationrequest/quotationrequest_form.html",{'form':form})
        else:
                if id==0:
                        form = QuotationRequestForm(request.POST)
                else:
                        quotationrequest = QuotationRequest.objects.get(pk=id)
                        form = QuotationRequestForm(request.POST,instance=quotationrequest)
                if form.is_valid():
                        form.save()
                return redirect('/quotationrequest/list')

#Delete Function
def quotationrequest_delete(request,id):
        quotationrequest = QuotationRequest.objects.get(pk=id)
        quotationrequest.delete()
        return redirect('/quotationrequest/list')