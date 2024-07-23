from django.urls import path, include
from .views import *

app_name = 'member'
urlpatterns = [
    path('info/', GetInfo.as_view()),
    path('info/detail/<int:user_id>/', UpdateUser.as_view()),
]