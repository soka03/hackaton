from django.db import models
from member.models import CustomUser
from boss.models import *

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='orders')
    order = models.IntegerField()
    body = models.TextField(default='')
    order_date = models.DateTimeField(auto_now_add=True)