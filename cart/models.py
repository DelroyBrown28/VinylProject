from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse




User = get_user_model()


class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.adress_line_1}, {self.adress_line_2},{self.city},"
    
    class Meta:
        verbose_name_plural = 'Adresses'
    

class FormatVariation(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    artist_name = models.CharField(max_length=150, null=False)
    album_title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images')
    image_2 = models.ImageField(upload_to='product_images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    available_formats = models.ManyToManyField(FormatVariation)
    
    def __str__(self):
        return self.artist_name

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={"slug": self.slug})
    
    

class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    format = models.ForeignKey(FormatVariation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product.artist_name} / {self.product.album_title} - {self.quantity}x"
    

class Order(models.Model):
    user = models.ForeignKey(User,
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    
    billing_address = models.ForeignKey(Address,
                                        related_name='billing_address',
                                        blank=True,
                                        null=True,
                                        on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(Address,
                                        related_name='shipping_address',
                                        blank=True,
                                        null=True,
                                        on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.reference_number
    
    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"
    
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('PayPal', 'PayPal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()
    
    def __str__(self):
        return self.reference_number
    
    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"
    
    
def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
   
pre_save.connect(pre_save_product_receiver, sender=Product)     
        