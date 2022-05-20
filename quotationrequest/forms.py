from django import forms
from .models import QuotationRequest

class QuotationRequestForm(forms.ModelForm):

    class Meta:
        model = QuotationRequest
        fields = ('number','duedate','notes','supplier','status','employee')
        labels = {
            'number':'Request Number',
            'duedate':'Due Date',
            'notes':'Special Notes',
            'supplier':'Civil Status',
            'status':'Designation',
            'employee':'Permanant Address',
        }


    def __init__(self, *args, **kwargs):
        super(QuotationRequestForm,self).__init__(*args, **kwargs)
        self.fields['supplier'].empty_label="Select Supplier"
        self.fields['status'].empty_label="Select Status"
        self.fields['employee'].empty_label="Added By"
        self.fields['notes'].required = False


