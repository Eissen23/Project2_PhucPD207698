
from rest_framework import serializers
from django.contrib.auth import get_user_model

from quanlydoan.auth.models import Giangvien, Sinhvien
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','fullName', 'email', 'is_teacher', )


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

class SinhvienSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sinhvien
        fields = ('masv', 'hoten', 'malop', 'sdt','nganh', ) 
        
class GiangvienSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Giangvien
        fields = ('magv', 'hotengb', 'vien', 'email',  )