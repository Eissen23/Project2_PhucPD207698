from rest_framework import serializers
from .models import Sinhvien, Giangvien, Nhom
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        model = User
        field = ('id', 'email', 'name', 'password')

class SinhvienSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sinhvien
        fields = ('masv', 'hoten', 'idnhom', 'malop', 'sdt', 'nganh', 'emailsv') 
        
class GiangvienSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Giangvien
        fields = ('magv', 'hotengb', 'vien', 'email')
        
class NhomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Nhom
        fields = ('idnhom', 'mamon', 'magv', 'term', 'tennhom', 'tendetai', 'projectstatus')

class CreateSinhvienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinhvien
        fields = ('masv', 'hoten', 'malop', 'sdt', 'nganh', 'emailsv')