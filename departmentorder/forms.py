from django import forms
from .models import DepartmentOrder
from datetimewidget.widgets import DateWidget

class DepartmentOrderForm(forms.ModelForm):

    class Meta:
        model = DepartmentOrder
        fields = ('number','department','orderdate','totalamount','notes','status')
        labels = {

            'number':'Dep. Order Number',
            'department':'Department',
            'orderdate':'Order Date',
            'totalamount':'Total Amount',
            'notes':'Notes',
            'regdate':'Added Date',
            'status':'Status',
        }

        widgets = {
            #Use localization and bootstrap 4
            'orderdate': DateWidget(attrs={'id':"orderdate"}, usel10n = True, bootstrap_version=4)
        }
    
    def __init__(self, *args, **kwargs):
        super(DepartmentOrderForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label="Select Department"
        self.fields['status'].empty_label="Select Status"
        self.fields['notes'].required = False


