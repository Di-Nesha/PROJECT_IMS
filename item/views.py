from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Create your PDF here.
def item_pdf(request):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont("Courier", 14)

        items = Item.objects.all()

        lines = []

        for item in items:
                lines.append(item.number)
                lines.append(item.name)
                lines.append(item.rop)
                lines.append(item.roq)
                lines.append(item.qty)
                lines.append(item.size)
                lines.append("-------------------------------------------")

        for line in lines:
                textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename="Item.pdf")


#Create your views here.
def item_list(request):
        context = {'item_list':Item.objects.all()}
        return render(request,"item/item_list.html",context)

# Insert & Update Function
def item_form(request, id=0):
        if request.method == "GET":
                if id==0:
                        form = ItemForm()
                else:
                        item = Item.objects.get(pk=id)
                        form = ItemForm(instance=item)
                return render(request,"item/item_form.html",{'form':form})
        else:
                if id==0:
                        form = ItemForm(request.POST)
                else:
                        item = Item.objects.get(pk=id)
                        form = ItemForm(request.POST,instance=item)
                if form.is_valid():
                        form.save()
                return redirect('/item/list')

#Delete Function
def item_delete(request,id):
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('/item/list')