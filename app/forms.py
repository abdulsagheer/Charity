from django import forms
from .models import Donator

class DonateModelForm(forms.ModelForm):
    class Meta:
        model=Donator
        fields=('name','email',)