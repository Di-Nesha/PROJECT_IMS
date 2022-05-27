from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation
        fields = ('number','validatefrom','validateto','quotationrequest','employee','status','notes')
        labels = {
            'number':'Quotation Number',
            'validatefrom':'Validate From',
            'validateto':'Validate From',
            'quotationrequest':'Quotation Request',
            'employee':'Added By',
            'status':'Quotation Status',
            'notes':'Special Notes',
            'regdate':'Register Date',
        }

    def __init__(self, *args, **kwargs):
        super(QuotationForm,self).__init__(*args, **kwargs)
        self.fields['quotationrequest'].empty_label="Select Quotation Request"
        self.fields['employee'].empty_label="Select Employee"
        self.fields['status'].empty_label="Select Status"
        self.fields['notes'].required = False


