
from django.db import models

from authentication.models import Giangvien, Sinhvien


class Mon(models.Model):
    mamon = models.CharField(primary_key=True, max_length=10) 
    tenmon = models.CharField(max_length=20, blank=True, null=True) 
        
class Mongiangvien(models.Model):
    magiangday = models.CharField(primary_key=True, max_length=8) 
    mamon = models.ForeignKey(Mon, models.DO_NOTHING, blank=True, null=True) 
    magv = models.ForeignKey(Giangvien, models.DO_NOTHING, blank=True, null=True) 

class Nhom(models.Model):
    idnhom = models.CharField( primary_key=True, max_length=5) 
    term = models.PositiveIntegerField( blank=True, null=True) 
    tennhom = models.CharField( max_length=10, blank=True, null=True) 
    tendetai = models.CharField( max_length=100, blank=True, null=True) 
    projectstatus = models.BooleanField( blank=True, null=True) 
    magiangday = models.ForeignKey(Mongiangvien, models.DO_NOTHING, blank=True, null=True) 

class Thanhviennhom(models.Model):
    mathamgia = models.CharField(db_column='MaThamGia', primary_key=True, max_length=8) 
    masv = models.ForeignKey(Sinhvien, models.DO_NOTHING, db_column='MaSV', blank=True, null=True) 
    idnhom = models.ForeignKey(Nhom, models.DO_NOTHING, db_column='IdNhom', blank=True, null=True) 