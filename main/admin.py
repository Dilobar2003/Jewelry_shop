from django.contrib import admin

from .models import BannerModel, ContactMessageModel

@admin.register(ContactMessageModel)
class ContactMessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']



@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_display_links = ['id', 'title']
