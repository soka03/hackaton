from django.db import models
from member.models import CustomUser
from boss.models import Post

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='orders')
    order = models.IntegerField()
    body = models.TextField(default='')
    order_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


