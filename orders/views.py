from typing import Any, Dict, Optional, Type
from django import http
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, reverse
from products.models import ProductModel
from django.views.generic import TemplateView, CreateView
from users.models import ProfileModel
from .forms import OrderModelForm
from django.db.models import Sum




class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm
    success_url = '/'


    def dispatch(self, request, *args, **kwargs):
        if len(self.request.session.get('cart', [])) == 0:
            return redirect(reverse('main:home')) 
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        if cart:
            products = ProductModel.get_cart_objects(cart)
            data['products'] = products

        if hasattr(self.request.user, 'profile'):
            data['profile'] = ProfileModel.objects.get(user=self.request.user)

        return data    
    
    
    def form_valid(self, form):
        cart = self.request.session.get('cart')
        products = ProductModel.get_cart_objects(cart)
        price = products.aggregate(Sum('real_price')).get('real_price_sum', '')

        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        form.instance.total_price = price
        order = form.save()
        order.prducts.set(products)
        self.request.session['cart'] = []
        return redirect(self.success_url)    
    





def shopping_cart_view(request):
    cart = request.session.get('cart', [])
    objects = ProductModel.get_cart_objects(cart)
    return render(request, 'main/shopping-cart.html', context={
        'objects' : objects
    })


def delete_cart_value_view(request, id):
    cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
        request.session['cart'] = cart
    return redirect(request.GET.get('next/', 'orders:shopping-cart'))
