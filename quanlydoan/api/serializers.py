from rest_framework import serializers
from .models import Nhom, Thanhviennhom, Mon, Mongiangvien

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
        
