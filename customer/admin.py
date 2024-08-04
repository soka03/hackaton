from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_product', 'customer', 'pickup_time', 'body', 'order',  'order_date')

    def get_user(self, obj):
        return obj.post.user.username
    get_user.short_description = 'User'

    def get_product(self, obj):
        return obj.post.product
    get_product.short_description = 'Product'
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'customer', 'rating', 'comment', 'created_at')