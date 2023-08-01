from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sinhvien, Giangvien, Nhom
from .serializers import UserSerializer, SinhvienSerializer, GiangvienSerializer
from django.contrib.auth import get_user_model
import traceback

User = get_user_model()

# Create your views here.

def insert_student(requested_data, user, fullName, email):
    hoten = fullName
    emailsv = email
    masv = requested_data['code']
    malop = requested_data['malop']
    sdt = requested_data['sdt']
    nganh= requested_data['domain']
    user_id = user
    
    sinhvien = Sinhvien(masv = masv, hoten = hoten,malop=malop ,emailsv = emailsv, sdt = sdt, nganh= nganh, user_id = user_id)
    sinhvien.save()
    
    return sinhvien

def insert_teacher(requested_data, user, fullName, email):
    magv = requested_data['code']
    hotengb = fullName
    teacher_email = email
    vien =  requested_data['domain']
    user_id = user
    
    giangvien = Giangvien(magv = magv, hotengb = hotengb, email = teacher_email, vien = vien, user_id = user_id)
    giangvien.save()
    
    return giangvien

class SignupView(APIView):
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
            
            if password ==  re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_teacher: 
                            user = User.objects.create_user(fullName=fullName, email=email, password=password)
                            insert_student(requested_data=data, user= user, fullName= fullName, email=email)
                            return Response(
                                {"success": "User successfully created"},
                                status= status.HTTP_201_CREATED
                            )
                        else: 
                            teacher = User.objects.create_teacher(fullName=fullName, email=email, password=password)
                            insert_teacher(requested_data=data, user = teacher, fullName=fullName, email=email)
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
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong!'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
     
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data['id']
            
            if not user.data['is_teacher']:
                user_detail = Sinhvien.objects.get(user_id = user_id) 
                detail = SinhvienSerializer(user_detail)
                
            else:
                user_detail = Giangvien.objects.get(user_id = user_id)
                detail = GiangvienSerializer(user_detail)
            
            return Response(
                {
                    'user': user.data,
                    'detail': detail.data
                },
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
# get the data of the corresponding user