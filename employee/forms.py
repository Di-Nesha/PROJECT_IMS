from django import forms
from .models import New

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = New
        fields = ('number','fullname','callingname','photo','nic','gender','civilstatus','designation','address','mobile','land','notes','employeestatus')
        labels = {
            'number':'Employee Number',
            'fullname':'Full Name',
            'callingname':'Calling Name',
            'photo':'Photo',
            'nic':'NIC',
            'gender':'Gender',
            'civilstatus':'Civil Status',
            'designation':'Designation',
            'address':'Permanant Address',
            'mobile':'Mobile Number',
            'land':'Land Number',
            'notes':'Special Notes',
            'employeestatus_id':'Employee Status',
            'regdate':'Register Date',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label="Select Gender"
        self.fields['civilstatus'].empty_label="Select Civil Status"
        self.fields['employeestatus'].empty_label="Select Employee Status"
        self.fields['designation'].empty_label="Select Designation"
        self.fields['photo'].required = False
        self.fields['notes'].required = False


