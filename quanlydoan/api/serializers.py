from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Sinhvien, Giangvien, Nhom, Thanhviennhom, Mon, Mongiangvien, Cuochop, Report
User = get_user_model()

class SignupSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    re_password = serializers.CharField(write_only=True, required=True)
    is_teacher = serializers.BooleanField(default=False)

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError({'re_password': 'Passwords do not match'})
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','fullName', 'email', 'is_teacher', )

class SinhvienSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sinhvien
        fields = ('masv', 'hoten', 'malop', 'sdt','nganh', ) 
        
class GiangvienSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Giangvien
        fields = ('magv', 'hotengb', 'vien', 'email',  )
        
class NhomSerializer (serializers.ModelSerializer):

    class Meta:
        model = Nhom
        fields = (  'term', 'tennhom', 'tendetai', 'magiangday')
        
class ThanhVienNhomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thanhviennhom        
        fields = ('masv', 'idnhom',)

class MonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mon
        fields = ('mamon', 'tenmon', )
        
class MonGiangVienSerializer (serializers.ModelSerializer):
    class Meta:
        model = Mongiangvien
        fields = ('magiangday', 'mamon', 'magv')
        
class CuocHopSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cuochop
        fields = ('idnhom', 'meettime', 'isreported','ghichu', )
        
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('codeurl','report', 'cuochop',)