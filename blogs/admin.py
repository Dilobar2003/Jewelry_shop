from django.contrib import admin

from .models import BlogModel, BlogTagsModel, CommentModel

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']



@admin.register(BlogTagsModel)
class BlogTagsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name', 'created_at']
    readonly_fields = ['name', 'email', 'phone', 'comment']