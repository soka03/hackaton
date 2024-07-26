from django.urls import path
from .views import *

app_name = 'customer'

urlpatterns = [
    path('order/<int:post_id>/request/', CreateOrderView.as_view()),
    path('order/<int:order_id>/', OrderDetailView.as_view()),
    path('order/<int:order_id>/delete/', DeleteOrderView.as_view()),
    path('<str:district>/', get_boards_by_location),
]