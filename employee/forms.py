from django import forms
from .models import Main

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Main
        fields = '__all__'