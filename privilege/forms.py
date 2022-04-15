from django import forms
from .models import Privilege

class PrivilegeForm(forms.ModelForm):

    class Meta:
        model = Privilege
        fields = ('sel','ins','upd','delt','role','module')
        labels = {
            'sel':'Select',
            'ins':'Insert',
            'upd':'Update',
            'delt':'Delete',
            'module':'Module',
            'role':'Role',
        }

    def __init__(self, *args, **kwargs):
        super(PrivilegeForm,self).__init__(*args, **kwargs)
        self.fields['module'].empty_label="Select Module"
        self.fields['role'].empty_label="Select Role"
        self.fields['sel'].required = False
        self.fields['ins'].required = False
        self.fields['upd'].required = False
        self.fields['delt'].required = False