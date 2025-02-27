
from rest_framework import serializers
from .models import *
from django.utils import timezone
from customer.models import *
from customer.serializers import *

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    city = serializers.CharField(source='user.city', read_only=True)
    district = serializers.CharField(source='user.district', read_only=True)
    dong = serializers.CharField(source='user.dong', read_only=True)
    detail_location = serializers.CharField(source='user.detail_location', read_only=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d %H:%M')
    
    def get_reviews(self, obj):
        orders = Order.objects.filter(post=obj)
        reviews = Review.objects.filter(order__in=orders)
        return ReviewSerializer(reviews, many=True).data

class PostSearchSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    city = serializers.CharField(source='user.city', read_only=True)
    district = serializers.CharField(source='user.district', read_only=True)
    dong = serializers.CharField(source='user.dong', read_only=True)
    detail_location = serializers.CharField(source='user.detail_location', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'nickname', 'city', 'district', 'dong', 'detail_location', 'created_at', 'image']

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d %H:%M')
    
    def get_reviews(self, obj):
        orders = Order.objects.filter(post=obj)
        reviews = Review.objects.filter(order__in=orders)
        return ReviewSerializer(reviews, many=True).data


class OrderCheckSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    nickname = serializers.CharField(source='user.nickname',read_only=True)
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d %H:%M')




