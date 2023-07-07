from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Sinhvien, Giangvien, Nhom
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','fullName', 'email', 'is_teacher', )

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
