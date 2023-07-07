from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sinhvien, Giangvien, Nhom
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
import traceback

User = get_user_model()

# Create your views here.


class SignupvView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        try:
            data = request.data
            
            fullName = data['fullName']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            
            # TODO: the logic in the signup
            is_teacher = data['is_teacher']
            
            if is_teacher == 'True':
                is_teacher = True
            else: 
                is_teacher = False    
            
            
            if password ==  re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_teacher: 
                            User.objects.create_user(fullName=fullName, email=email, password=password)
                            return Response(
                                {"success": "User successfully created"},
                                status= status.HTTP_201_CREATED
                            )
                        else: 
                            User.objects.create_teacher(fullName=fullName, email=email, password=password)
                            return Response(
                                {"success": "Teacher successfully created"},
                                status= status.HTTP_201_CREATED
                            )
                    else:
                        return Response(
                        {'error': 'Email already exist'},
                        status= status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                    {'error': 'Password must have more than 8 character'},
                    status= status.HTTP_400_BAD_REQUEST
                    )
                    
            else:
                return Response(
                    {'error': 'Password do not match'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong!'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )