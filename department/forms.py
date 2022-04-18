from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('number','name','land','email','fax','address','notes','status','employee')
        labels = {
            'number':'Department Number',
            'name':'Department',
            'land':'Telephone',
            'email':'Email',
            'fax':'FAX',
            'address':'Address',
            'notes':'Notes',
            'regdate':'Register Date',
            'status':'Department Status',
            'employee':'Added By',
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label="Select Status"
        self.fields['employee'].empty_label="Select Employee"
        self.fields['notes'].required = False


