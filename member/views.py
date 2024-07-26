from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView

class GetInfo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request):
        try:
            user = request.user
            self.check_object_permissions(self.request, user)
            serializer = CustomUserInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UpdateUser(APIView):
    def patch(self, request, user_id):
        try :
            user = CustomUser.objects.get(id=user_id)
            serializer = CustomUserInfoSerializer(user, data=request.data, partial=True)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

        username = request.data.get('username')
        nickname = request.data.get('nickname')
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        district = request.data.get('district')
        dong = request.data.get('dong')
        detail_location = request.data.get('detail_location')
        seller = request.data.get('seller')

        if username is not None:
            user.username = username
        if nickname is not None:
            user.nickname = nickname
        if phone_number is not None:
            user.phone_number = phone_number
        if city is not None:
            user.city = city
        if district is not None:
            user.district = district
        if detail_location is not None:
            user.detail_location = detail_location

        if seller is not None:
            user.seller = seller

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)