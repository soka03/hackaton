from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    nickname = serializers.ReadOnlyField(source='board.user.nickname')
    product = serializers.ReadOnlyField(source='board.product')
    price = serializers.ReadOnlyField(source='board.price')
    order_date = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'customer', 'nickname', 'location', 'product', 'order', 'price']
    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d %H:%M')