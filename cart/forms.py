from django import forms
from .models import OrderItem, Product


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['quantity']
