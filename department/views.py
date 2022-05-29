from django.shortcuts import render,redirect
from .forms import DepartmentForm
from .models import Department

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def department_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        departments = Department.objects.all()

        lines = []

        for department in departments:
                lines.append(department.number)
                lines.append(department.name)
                lines.append(department.land)
                lines.append(department.email)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Department.pdf")

#Create your views here.
def department_list(request):
        context = {'department_list':Department.objects.all()}
        return render(request,"department/department_list.html",context)

# Insert & Update Function
def department_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = DepartmentForm()
                else:
                        department = Department.objects.get(pk=id)
                        form = DepartmentForm(instance=department)
                return render(request,"department/department_form.html",{'form':form})
        else:
                if id==0:
                        form = DepartmentForm(request.POST)
                else:
                        department = Department.objects.get(pk=id)
                        form = DepartmentForm(request.POST,instance=department)
                if form.is_valid():
                        form.save()
                return redirect('/department/list')

#Delete Function
def department_delete(request,id):
        department = Department.objects.get(pk=id)
        department.delete()
        return redirect('/department/list')
        