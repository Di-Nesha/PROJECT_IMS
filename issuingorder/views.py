from django.shortcuts import render,redirect
from .forms import IssuingOrderForm
from .models import IssuingOrder, Item

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def issuing_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        issuings = IssuingOrder.objects.all()

        lines = []

        for issuing in issuings:
                lines.append(issuing.number)
                lines.append(issuing.departmentorder.number)
                lines.append(issuing.employee.callingname)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Issuing-Order.pdf")

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