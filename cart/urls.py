from django.urls import path
from cart.views import ProductDetailView
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug>/', views.ProductDetailView.as_view(), name='product-detail')
    
]