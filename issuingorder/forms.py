from django import forms
from .models import IssuingOrder

class IssuingOrderForm(forms.ModelForm):

    class Meta:
        model = IssuingOrder
        fields = ('number','item','totalamount','discountratio','netamount','notes','status','employee','departmentorder')
        labels = {

            'number':'Order  Number',
            'item':'Item',
            'totalamount':'Total Amount',
            'discountratio':'Discount Ratio',
            'netamount':'Net Amount',
            'notes':'Notes',
            'status':'Status',
            'employee':'Added By',
            'departmentorder':'Dep. Order No',
        }

    def __init__(self, *args, **kwargs):
        super(IssuingOrderForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label="Select Status"
        self.fields['employee'].empty_label="Select Employee"
        self.fields['departmentorder'].empty_label="Select Dep.Order Number"
        self.fields['discountratio'].required = False


