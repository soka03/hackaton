from rest_framework import serializers
from .models import *
from boss.models import Post


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
        
        
class PostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'product', 'price', 'user']


class ReviewSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(write_only=True, required=False)
    post = PostInfoSerializer(source='order.post', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'order_id', 'post','customer', 'content', 'rating', 'created_at']
        read_only_fields = ['customer', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['customer'] = request.user
        order_id = validated_data.pop('order_id', None)
        if order_id:
            order = Order.objects.get(id=order_id, customer=request.user)
        else:
            order = Order.objects.filter(customer=request.user).first()

        validated_data['order'] = order

        return super().create(validated_data)
    
