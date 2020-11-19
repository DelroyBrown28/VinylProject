from django.contrib import admin
from .models import (FormatVariation,
                    Order,
                    OrderItem,
                    Product,
                    Address,
                    Payment,
                    Category)


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'zip_code',
        'city',
        'address_type',
    ]
    
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['artist_name']
    list_filter = ['primary_category']
    prepopulated_fields = {"slug": ("album_title", "artist_name")}
    class Meta:
        model = Product


admin.site.register(Category)
admin.site.register(Address, AddressAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(FormatVariation)
admin.site.register(Payment)
