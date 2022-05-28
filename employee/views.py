from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import EmployeeForm
from .models import New

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



#Create your PDF here.
def genarate_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)


        employees = New.objects.all()

        lines = []

        for employee in employees:
                lines.append(employee.number)
                lines.append(employee.fullname)
                lines.append(employee.nic)
                lines.append(employee.mobile)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Employee.pdf")

#Create your views here.
def employee_list(request):
        context = {'employee_list':New.objects.all()}
        return render(request,"employee/employee_list.html",context)

# Insert & Update Function
def employee_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = EmployeeForm()
                else:
                        employee = New.objects.get(pk=id)
                        form = EmployeeForm(instance=employee)
                return render(request,"employee/employee_form.html",{'form':form})
        else:
                if id==0:
                        form = EmployeeForm(request.POST)
                else:
                        employee = New.objects.get(pk=id)
                        form = EmployeeForm(request.POST,instance=employee)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Employee details submitted successfully.')
                return redirect('/employee/list')

#Delete Function
def employee_delete(request,id):
        employee = New.objects.get(pk=id)
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('/employee/list')