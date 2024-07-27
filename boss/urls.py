from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'boss'
urlpatterns = [
    path('', BossPost.as_view()),
    path('post/', Posting.as_view()),
    path('post/<int:post_id>/', PostingDetail.as_view()),
    path('<int:post_id>/order/', OrderCheck.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)