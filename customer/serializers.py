from rest_framework import serializers
from django.utils import timezone
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    nickname = serializers.ReadOnlyField(source='post.user.nickname')
    product = serializers.ReadOnlyField(source='post.product')
    price = serializers.ReadOnlyField(source='post.price')
    order_date = serializers.SerializerMethodField()
    class Meta:
        model = Order
        exclude = ['post']
    def get_order_date(self, obj):
        time = timezone.localtime(obj.order_date)
        return time.strftime('%Y-%m-%d %H:%M')