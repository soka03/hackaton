from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    nickname = models.CharField(max_length=100)
    """
    LOCATION_CHOICES = [
        ('강남구', '강남구'),
        ('강동구', '강동구'),
        ('강북구', '강북구'),
        ('강서구', '강서구'),
        ('관악구', '관악구'),
        ('광진구', '광진구'),
        ('구로구', '구로구'),
        ('금천구', '금천구'),
        ('노원구', '노원구'),
        ('도봉구', '도봉구'),
        ('동대문구', '동대문구'),
        ('동작구', '동작구'),
        ('마포구', '마포구'),
        ('서대문구', '서대문구'),
        ('서초구', '서초구'),
        ('성동구', '성동구'),
        ('성북구', '성북구'),
        ('송파구', '송파구'),
        ('양천구', '양천구'),
        ('영등포구', '영등포구'),
        ('용산구', '용산구'),
        ('은평구', '은평구'),
        ('종로구', '종로구'),
        ('중구', '중구'),
        ('중랑구', '중랑구'),
    ]
    location = models.CharField(max_length=200, default="", choices=LOCATION_CHOICES)
    """
    city = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    dong = models.CharField(max_length=100, default="")
    detail_location = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=11, default="")

    SELLER_CHOICES = [
        ('판매자', '판매자'),
        ('구매자', '구매자'),
    ]
    seller = models.CharField(max_length=200, default="", choices=SELLER_CHOICES)