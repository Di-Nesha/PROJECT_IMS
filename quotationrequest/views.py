from django.shortcuts import render,redirect
from .forms import QuotationRequestForm
from .models import QuotationRequest

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def bidrequest_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        bidrequests = QuotationRequest.objects.all()

        lines = []

        for bidrequest in bidrequests:
                lines.append(bidrequest.number)
                lines.append(bidrequest.supplier.name)
                lines.append(bidrequest.status.name)
                lines.append(bidrequest.employee.callingname)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Bid-Request.pdf")

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