from django.shortcuts import render,redirect
from .forms import InventoryForm
from .models import Inventory

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def inventory_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        inventorys = Inventory.objects.all()

        lines = []

        for inventory in inventorys:
                # lines.append(inventory.availableqty)
                lines.append(inventory.status.name)
                lines.append(inventory.employee.callingname)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Inventory.pdf")

#Create your views here.
def inventory_list(request):
        context = {'inventory_list':Inventory.objects.all()}
        return render(request,"inventory/inventory_list.html",context)

# Insert & Update Function
def inventory_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = InventoryForm()
                else:
                        inventory = Inventory.objects.get(pk=id)
                        form = InventoryForm(instance=inventory)
                return render(request,"inventory/inventory_form.html",{'form':form})
        else:
                if id==0:
                        form = InventoryForm(request.POST)
                else:
                        inventory = Inventory.objects.get(pk=id)
                        form = InventoryForm(request.POST,instance=inventory)
                if form.is_valid():
                        form.save()
                return redirect('/inventory/list')

#Delete Function
def inventory_delete(request,id):
        inventory = Inventory.objects.get(pk=id)
        inventory.delete()
        return redirect('/inventory/list')