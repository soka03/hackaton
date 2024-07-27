from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'product', 'close', 'quantity', 'price', 'created_at')
