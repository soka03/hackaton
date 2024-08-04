from django.db import models
from member.models import CustomUser

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    product = models.CharField(max_length=50)
    close = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    body = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='', null=True, blank=True)