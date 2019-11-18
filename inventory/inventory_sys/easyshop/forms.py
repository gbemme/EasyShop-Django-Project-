from django import forms
from .models import Product,Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields =('card_no','card_type','address')
        color = ('blue')
