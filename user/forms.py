from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('status','displayname','username','email','password','employee','role',)
        labels = {
            'displayname':'Display Name',
            'username':'User Name',
            'email':'Email',
            'password':'Password',
            'status':'User Status',
            'employee':'Added By',
            'role':'User Role',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label="Select Status"
        self.fields['employee'].empty_label="Select Employee"
        self.fields['role'].empty_label="Select Role"