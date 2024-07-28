from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, ListView
from .models import BannerModel, WishListModel
from .forms import ContactForm
from django.views.generic import CreateView
from products.models import ProductModel



def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)
    request.session['cart'] = cart    
    return redirect(request.GET.get('next', '/'))            



class WishlistListView(ListView):
    template_name = 'main/wishlist.html'

    def get_queryset(self):
        return ProductModel.objects.filter(wishlistmodel__user=self.request.user)

def wishlist_view(request, id):
    product = ProductModel.objects.get(id=id)
    WishListModel.create_or_delete(request.user, product)
    path = request.GET.get('next')
    return redirect(path)

    
class ContactView(TemplateView):
    template_name = 'main/contact.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('main:contact')




class HomeView(TemplateView):

    template_name = 'main/index.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.filter(status=True)
        return context