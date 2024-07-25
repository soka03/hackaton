from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import CustomUser
import re

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)
    phonenumber = serializers.CharField(max_length=20) #Integer로 받으니까 앞에 0이 사라짐
    location = serializers.CharField(max_length=100)
    #location = serializers.ChoiceField(choices=CustomUser.LOCATION_CHOICES)
    seller = serializers.ChoiceField(choices=CustomUser.SELLER_CHOICES)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'phonenumber': self.validated_data.get('phonenumber', ''),
            'location': self.validated_data.get('location', ''),
            'seller': self.validated_data.get('seller', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.nickname = self.cleaned_data.get('nickname')
        user.phonenumber = self.cleaned_data.get('phonenumber')
        user.location = self.cleaned_data.get('location')
        user.seller = self.cleaned_data.get('seller')

        ###########
        location = self.cleaned_data.get('location', '')
        district = self.extract_district(location)
        user.district = district

        user.save()
        adapter.save_user(request, user, self)
        return user

    ###########
    def extract_district(self, location):
        pattern = re.compile(r'\b구\b')  # '구'라는 단어가 있는 위치에서 추출할 수 있도록 정규표현식 패턴 설정
        match = pattern.search(location)
        if match:
            district = location[match.start():match.end()]  # 구의 위치에서부터 추출
            return district.strip()
        else:
            return ''

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname', 'phonenumber', 'location', 'seller', 'district']

class CustomUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'nickname', 'phonenumber', 'location', 'seller', 'district']
    