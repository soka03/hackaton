from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)
    #location = serializers.ChoiceField(choices=CustomUser.LOCATION_CHOICES)
    phone_number = serializers.CharField(max_length=11, default="")

    city = serializers.CharField(max_length=100, default="")
    district = serializers.CharField(max_length=100, default="")
    dong = serializers.CharField(max_length=100, default="")
    detail_location = serializers.CharField(max_length=100, default="")
    seller = serializers.ChoiceField(choices=CustomUser.SELLER_CHOICES)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'city': self.validated_data.get('city', ''),
            'district': self.validated_data.get('district', ''),
            'dong': self.validated_data.get('dong', ''),
            'detail_location': self.validated_data.get('detail_location', ''),
            'seller': self.validated_data.get('seller', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.nickname = self.cleaned_data.get('nickname')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.city = self.cleaned_data.get('city')
        user.district = self.cleaned_data.get('district')
        user.dong = self.cleaned_data.get('dong')
        user.detail_location = self.cleaned_data.get('detail_location')
        user.seller = self.cleaned_data.get('seller')
        user.save()
        adapter.save_user(request, user, self)
        return user
    

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'phone_number','nickname', 'city', 'district', 'dong', 'detail_location', 'seller']

class CustomUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number' 'nickname', 'city', 'district', 'dong', 'detail_location', 'seller']
    
"""
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.location = validated_data.get('location', instance.location)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.save()
        return instance
"""