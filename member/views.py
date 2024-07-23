from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
#from rest_framework.decorators import api_view, authentication_classes, permission_classes

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
    
    def patch(self, request):
        try:
            user = request.user
            self.check_object_permissions(self.request, user)
            serializer = CustomUserInfoSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
               return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)