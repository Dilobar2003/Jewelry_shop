from django.urls import path
from .views import shopping_cart_view, delete_cart_value_view, CheckoutView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shopping-cart/', shopping_cart_view, name='shopping-cart'),
    path('delete-cart-value/<int:id>/', delete_cart_value_view, name='delete-cart')
]