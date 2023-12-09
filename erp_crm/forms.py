from . models import Service, Customer, Payment, Payment_Record_Status
from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model  = Service
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class Payment_Record_StatusForm(forms.ModelForm):
    class Meta:
        model = Payment_Record_Status
        fields = '__all__'