from typing import Any, Dict
from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel, CategoryModel, ProductTagModel, ProductSizeModel, BrandModel


class ProductListView(ListView):
    template_name = 'main/shop.html'
    paginate_by = 9


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['sizes'] = ProductSizeModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['min'], context['max'] = ProductModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()
        return context


    def get_queryset(self):
       qs = ProductModel.objects.all()
       q = self.request.GET.get('q')
       if q:
           qs = qs.filter(title__icontains=q)
       cat = self.request.GET.get('cat')  
       if cat:
           qs = qs.filter(category=cat)    

       brand = self.request.GET.get('brand')
       if brand:
           qs = qs.filter(brand=brand)

       tag = self.request.GET.get('tag')
       if tag:
           qs = qs.filter(tags=tag)
       size = self.request.GET.get('size')   
       if size:
           qs = qs.filter(size=size)
       price = self.request.GET.get('price')    
       if price:
           min, max = price.split(';') # ['150', '325'] min >= real_price and max <= real_price
           qs = qs.filter(real_price__gte=min, real_price__lte=max)

              
    
       return qs
    

