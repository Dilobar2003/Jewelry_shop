from django import template
from main.models import WishListModel
from products.models import ProductModel
from django.db.models import Sum

register = template.Library()


@register.filter()
def is_cart(product, request):
    cart = request.session.get('cart', [])
    return product.id in cart

@register.simple_tag()
def get_cart_info(request):
    cart = request.session.get('cart', [])
    if not cart:
        return 0, 0.0
    return len(cart),  ProductModel.get_cart_objects(cart).aggregate(Sum('real_price'))['real_price__sum']

@register.simple_tag()
def get_current_price(request, x):
    data = request.GET.get('price')
    if data:
        return data.split(';')[x]
    else:
        return 'null'

@register.filter()
def is_wishlist(user, product):
    return WishListModel.objects.filter(user=user, product=product).exists()