from django.contrib import admin
from .models import Travel, Comment
# Register your models here.

@admin.register(Travel)
class TravelModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'image', 'image_second', 'created_at')
    list_filter = ('region', )
    search_fields = ('title', 'region', )



@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('travel', 'post', 'author', 'secret', 'created_at')
    list_filter = ('secret', )
    search_fields = ('travel__title', 'post__title')