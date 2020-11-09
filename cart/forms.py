from django.contrib.auth import get_user_model
from django import forms
from .models import FormatVariation, OrderItem, Product, Address


User = get_user_model()


class AddToCartForm(forms.ModelForm):
    format = forms.ModelChoiceField(queryset=FormatVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'format']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['format'].queryset = product.available_formats.all()


class AddressForm(forms.Form):
    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    
    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    shipping_address_1 = forms.CharField()
    shipping_address_2 = forms.CharField()
    shipping_zip_code = forms.CharField()
    shipping_city = forms.CharField()
    billing_address_1 = forms.CharField()
    billing_address_2 = forms.CharField()
    billing_zip_code = forms.CharField()
    billing_city = forms.CharField()


    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)


        user = User.objects.get(id=user_id)

        shipping_address_queryset = Address.objects.filter(
            user=user,
            address_type='S'
        )

        billing_address_queryset = Address.objects.filter(
            user=user,
            address_type='B'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_queryset
        self.fields['selected_billing_address'].queryset = billing_address_queryset

    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_1', None):
                self.add_error("shipping_address_1", "Please fill in this field")
            if not data.get('shipping_address_2', None):
                self.add_error("shipping_address_2", "Please fill in this field")
            if not data.get('shipping_zip_code', None):
                self.add_error("shipping_zip_code", "Please fill in this field")
            if not data.get('shipping_city', None):
                self.add_error("shipping_city", "Please fill in this field")

        selected_billing_address = data.get('selected_billing_address', None)
        if selected_billing_address is None:
            if not data.get('billing_address_1', None):
                self.add_error("shipping_address_1", "Please fill in this field")
            if not data.get('billing_address_2', None):
                self.add_error("shipping_address_2", "Please fill in this field")
            if not data.get('billing_zip_code', None):
                self.add_error("shipping_zip_code", "Please fill in this field")
            if not data.get('billing_city', None):
                self.add_error("shipping_city", "Please fill in this field")



