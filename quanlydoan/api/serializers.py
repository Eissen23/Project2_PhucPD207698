from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Sinhvien, Giangvien, Nhom, Thanhviennhom, Mon, Mongiangvien, Cuochop
User = get_user_model()



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
        fields = ('idnhom', 'meettime', 'isnoted',  )