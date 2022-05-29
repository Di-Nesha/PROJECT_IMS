from django.shortcuts import render,redirect
from .forms import QuotationForm
from .models import Quotation

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def quotation_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        quotations = Quotation.objects.all()

        lines = []

        for quotation in quotations:
                lines.append(quotation.number)
                lines.append(quotation.status.name)
                lines.append(quotation.quotationrequest.number)
                lines.append(quotation.employee.callingname)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Quotation.pdf")

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