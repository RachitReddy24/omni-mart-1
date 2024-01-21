from django import forms
from .models import Order
from django.forms import ModelForm, inlineformset_factory, formset_factory
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
                    'first_name':forms.Textarea(attrs={'placeholder': 'First Name', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px; padding:6px;','id': 'first_name'}),
                    'last_name':forms.Textarea(attrs={'placeholder': 'Last Name ', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:6px;','id': 'last_name'}),
                    'email':forms.Textarea(attrs={'placeholder': 'Email', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:3px;','id': 'email'}),
                    'phone_number':forms.Textarea(attrs={'placeholder': 'Phone Number', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:3px;','id': 'phone_number'}),
                    'address':forms.Textarea(attrs={'placeholder': 'Adress', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:3px;','id': 'address'}),
                    'postal_code':forms.Textarea(attrs={'placeholder': 'Postal Code', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:3px;','id': 'postal_code'}),
                    'city':forms.Textarea(attrs={'placeholder': 'City', 'style': 'font-size: 16px; font-weight: 500; width: 70%; height: 25px;padding:3px;','id': 'city'}),
                    
                }
        
Productformset = formset_factory(form=OrderCreateForm, extra=1)

