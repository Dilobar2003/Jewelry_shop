from django.contrib import admin

from .models import ProductModel, ProductSizeModel, ProductTagModel, CategoryModel, BrandModel

@admin.register(ProductModel)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'real_price', 'discount']
    list_display_links = ['id', 'title', 'real_price', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['real_price']



@admin.register(CategoryModel)

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['name']    


@admin.register(ProductSizeModel)

class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']    

   



@admin.register(ProductTagModel)

class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']      


@admin.register(BrandModel)

class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']    



