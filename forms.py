# forms.py
from django import forms
from .models import customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['customer_name', 'contact_number', 'address', 'email']
