from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = 'cart/product_detail.html'
    queryset = Product.objects.all()