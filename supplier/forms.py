from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('number','name','mobile','land','email','cpname','address','cpnumber','creditlimit','tobepaid','remarks','bhname','bankname','baccountno','bbranch','status','employee')
        labels = {

            'number':'Supplier Number',
            'name':'Contact Person',
            'mobile':'Contact No',
            'land':'Office Phone',
            'email':'Email',
            'cpname':'Company Name',
            'address':'Company Address',
            'creditlimit':'Credit Limit',
            'tobepaid':'To Be Paid',
            'remarks':'Remarks',
            'bhname':'Bank Holder Name',
            'bankname':'Bank Name',
            'baccountno':'Account No',
            'bbranch':'Branch',
            'status':'Supplier Status',
            'employee':'Registered By',
            'regdate':'Register Date',
        }

    def __init__(self, *args, **kwargs):
        super(SupplierForm,self).__init__(*args, **kwargs)
        self.fields['bankname'].empty_label="Select Bank"
        self.fields['status'].empty_label="Select Status"
        self.fields['employee'].empty_label="Select Employee"
        self.fields['tobepaid'].required = False
        self.fields['remarks'].required = False


