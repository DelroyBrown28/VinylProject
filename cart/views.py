from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()