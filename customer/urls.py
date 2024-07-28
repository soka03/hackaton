from django.urls import path
from .views import *

app_name = 'customer'

urlpatterns = [
    path('order/<int:post_id>/request/', CreateOrderView.as_view()),
    path('order/<int:order_id>/', OrderDetailView.as_view()),
    path('order/<int:order_id>/delete/', DeleteOrderView.as_view()),
    path('<str:dong>/', get_boards_by_location),
    path('order/<int:order_id>/review/', CreateReviewView.as_view(), name='create-review'),
    path('review/<int:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
]