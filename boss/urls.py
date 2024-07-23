from django.urls import path
from .views import *

app_name = 'boss'
urlpatterns = [
    path('', BossPost.as_view()),
    path('post/', Posting.as_view()),
    path('post/<int:post_id>/', PostingDetail.as_view()),
    path('<int:post_id>/order/', OrderCheck.as_view()),
]