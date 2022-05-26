from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('availableqty','notes','status','employee')
        labels = {
            'availableqty':'Available Qty',
            'notes':'Remarks',
            'status':'Status',
            'employee':'Added By',
            'regdate':'Register Date',
        }

    def __init__(self, *args, **kwargs):
        super(InventoryForm,self).__init__(*args, **kwargs)
        self.fields['employee'].empty_label="Added By"
        self.fields['status'].empty_label="Select Status"
        self.fields['notes'].required = False


