from django.urls import path
from .views import HomeView, ContactView, ContactCreateView, wishlist_view, WishlistListView, add_to_cart




app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wishlist/<int:id>/', wishlist_view, name='wishlist'),
    path('add-cart/<int:id>/', add_to_cart, name='add-cart'),
    path('wishlist-list/', WishlistListView.as_view(), name='wishlist-list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create')


]

