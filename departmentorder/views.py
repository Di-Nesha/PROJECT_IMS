from django.shortcuts import render,redirect
from .forms import DepartmentOrderForm
from .models import DepartmentOrder

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def depodr_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        depodrs = DepartmentOrder.objects.all()

        lines = []

        for depodr in depodrs:
                lines.append(depodr.number)
                lines.append(depodr.department.name)
                lines.append(depodr.status.name)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Department-Order.pdf")

#Create your views here.
def departmentorder_list(request):
        context = {'departmentorder_list':DepartmentOrder.objects.all()}
        return render(request,"departmentorder/departmentorder_list.html",context)

# Insert & Update Function
def departmentorder_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = DepartmentOrderForm()
                else:
                        departmentorder = DepartmentOrder.objects.get(pk=id)
                        form = DepartmentOrderForm(instance=departmentorder)
                return render(request,"departmentorder/departmentorder_form.html",{'form':form})
        else:
                if id==0:
                        form = DepartmentOrderForm(request.POST)
                else:
                        departmentorder = DepartmentOrder.objects.get(pk=id)
                        form = DepartmentOrderForm(request.POST,instance=departmentorder)
                if form.is_valid():
                        form.save()
                return redirect('/departmentorder/list')

#Delete Function
def departmentorder_delete(request,id):
        departmentorder = DepartmentOrder.objects.get(pk=id)
        departmentorder.delete()
        return redirect('/departmentorder/list')