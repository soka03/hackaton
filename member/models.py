from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    nickname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
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
        ('중랄구', '중랄구'),
    ]
    location = models.CharField(max_length=200, default="", choices=LOCATION_CHOICES)
    """

    #postalcode = models.CharField(max_length=10)
    location = models.CharField(max_length=200) #주소
    #location_ = models.CharField(max_length=100) #참고
    #address = models.CharField(max_length=200) #상세주소
    district = models.CharField(max_length=50, blank=True, null=True)  #구정보 저장필드
    
    SELLER_CHOICES = [
        ('판매자', '판매자'),
        ('구매자', '구매자'),
    ]
    seller = models.CharField(max_length=200, default="", choices=SELLER_CHOICES)
