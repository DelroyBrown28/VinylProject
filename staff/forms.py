from django import forms
from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'artist_name',
            'album_title',
            'image',
            'image_2',
            'price',
            'available_formats',
        ]
