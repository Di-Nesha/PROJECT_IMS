from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('number','category','subcategory','brand','name','size','unittype','qty','unitprice','photo','roq','rop','remarks', 'status', 'employee')
        labels = {
            'number':'Item Number',
            'category':'Category',
            'subcategory':'Sub Category',
            'brand':'Brand',
            'name':'Name',
            'size':'Size',
            'unittype':'Unit Type',
            'qty':'Quantity',
            'unitprice':'Unit Price',
            'photo':'Photo',
            'roq':'Re-Order Qty',
            'rop':'Re-Order Point',
            'remarks':'Special Notes',
            'status':'Item Status',
            'employee':'Registered By',
            'regdate':'Register Date',
        }

    def __init__(self, *args, **kwargs):
        super(ItemForm,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label="Select Category"
        self.fields['subcategory'].empty_label="Select Sub Category"
        self.fields['brand'].empty_label="Select Brand"
        self.fields['unittype'].empty_label="Select Unit Type"
        self.fields['status'].empty_label="Select Item Status"
        self.fields['employee'].empty_label="Registered By"
        self.fields['photo'].required = False
        self.fields['size'].required = False
        self.fields['remarks'].required = False


