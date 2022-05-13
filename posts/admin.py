from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'body', 'created_at')
    search_fields = ('user__user__username', 'title')       # Profile 모델의 user - User 모델의 username 조회
