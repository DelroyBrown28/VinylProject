from django.contrib import admin
from .models import FormatVariation, Order, OrderItem, Product


admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(FormatVariation)
