from django import forms
from .models import *


class RegisterForms(forms.ModelForm):

    class Meta:

        model = Data

        fields = "__all__" #["name","contact","address","email"]
        
        widgets = {
            "name"   :forms.TextInput(attrs={'class':'form-control'}),
            "contact":forms.TextInput(attrs={'class':'form-control'}),
            "address":forms.TextInput(attrs={'class':'form-control'}),
            "email"  :forms.TextInput(attrs={'class':'form-control'}),
        }