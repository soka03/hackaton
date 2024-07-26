from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    nickname = serializers.ReadOnlyField(source='post.user.nickname')
    product = serializers.ReadOnlyField(source='post.product')
    price = serializers.ReadOnlyField(source='post.price')
    city = serializers.CharField(source='customer.city', read_only=True)
    district = serializers.CharField(source='customer.district', read_only=True)
    dong = serializers.CharField(source='customer.dong', read_only=True)
    detail_location = serializers.CharField(source='customer.detail_location', read_only=True)

    order_date = serializers.DateTimeField(format = '%Y-%m-%d %H:%M', read_only = True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'nickname', 'city', 'district', 'dong', 'detail_location', 'body', 'product', 'order', 'price', 'order_date']