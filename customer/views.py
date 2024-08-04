from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import OrderSerializer
from boss.models import *
from member.models import CustomUser
from boss.serializers import *
from rest_framework.decorators import api_view

class CreateOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, post_id): #주문 작성
        post = get_object_or_404(Post, id=post_id)
        order = request.data.get('order', None)
        city = request.data.get('city', None)
        district = request.data.get('district', None)
        dong = request.data.get('dong', None)
        pickup_time = request.data.get('pickup_time', None)
        body = request.data.get('body', "")
        data = {
            'post': post.id,
            'order': order,
            'city': city,
            'district': district,
            'dong': dong,
            'pickup_time' : pickup_time,
            'body': body
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            order = serializer.save(customer=request.user, post=post)
            order_data = OrderSerializer(order).data
            return Response(order_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView): #주문 상세 조회
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteOrderView(APIView): #주문 삭제
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if order.customer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UpdateOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if order.customer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        data = request.data
        serializer = OrderSerializer(order, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOrdersByUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(f"Authenticated user: {user}")  # 추가된 디버깅 코드

        orders = Order.objects.filter(customer=user)
        print(f"Orders: {orders}")  # 추가된 디버깅 코드

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""
@api_view(['GET'])
def get_boards_by_location(request, dong): #지역별 판매글 목록 조회
    posts = Post.objects.filter(user__dong=dong)
    serializer = PostSearchSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
"""

@api_view(['GET'])
def get_boards_by_location(request, dong):
    posts = Post.objects.filter(user__dong=dong)
    
    latest_posts = {}
    for post in posts:
        user_id = post.user.id
        if user_id not in latest_posts or post.created_at > latest_posts[user_id].created_at:
            latest_posts[user_id] = post
    
    latest_posts_list = list(latest_posts.values())

    serializer = PostSearchSerializer(latest_posts_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CreateReviewView(APIView): # 리뷰 작성
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if order.customer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if hasattr(order, 'review'):
            return Response({'detail': 'This order already has a review.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'order': order.id, 
            'rating': request.data.get('rating'),
            'comment': request.data.get('comment')
        }
        
        serializer = ReviewSerializer(data=data, context={'request': request}) 
        if serializer.is_valid():
            review = serializer.save()
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailView(APIView): # 리뷰 조회, 수정, 삭제
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if review.customer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        data = {
            'rating': request.data.get('rating', review.rating),
            'comment': request.data.get('comment', review.comment)
        }
        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            updated_review = serializer.save()
            return Response(ReviewSerializer(updated_review).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if review.customer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetPostsByUser(APIView):
    def get(self, request, user_id):
        posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SellerReviewListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id, *args, **kwargs):
        posts = Post.objects.filter(user_id=user_id)
        orders = Order.objects.filter(post__in=posts)
        reviews = Review.objects.filter(order__in=orders)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)