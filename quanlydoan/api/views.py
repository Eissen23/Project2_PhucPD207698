from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sinhvien, Giangvien, Nhom
from .serializers import SinhvienSerializer, GiangvienSerializer, NhomSerializer, CreateSinhvienSerializer
# Create your views here.
class CreateSinhvienView(APIView):
    serializer_class = CreateSinhvienSerializer
    
    def post(self, request, format= None):
        pass
