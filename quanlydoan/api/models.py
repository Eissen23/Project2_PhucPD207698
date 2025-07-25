#  This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from auth.models import UserAccount

class Giangvien(models.Model):
    magv = models.CharField( primary_key=True, max_length=10) 
    hotengb = models.CharField( max_length=40, blank=True, null=True) 
    vien = models.CharField(max_length=100, blank=True, null=True) 
    email = models.CharField( max_length=50, blank=True, null=True) 
    user_id = models.ForeignKey(UserAccount, models.CASCADE)

class Sinhvien(models.Model):
    masv = models.CharField(primary_key=True, max_length=8) 
    hoten = models.CharField( max_length=40, blank=True, null=True) 
    malop = models.CharField( max_length=20, blank=True, null=True) 
    sdt = models.CharField( max_length=10, blank=True, null=True) 
    nganh = models.CharField( max_length=50, blank=True, null=True) 
    emailsv = models.CharField( max_length=50, blank=True, null=True) 
    user_id = models.ForeignKey(UserAccount, models.CASCADE)

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

class Cuochop(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idnhom = models.ForeignKey(Nhom, models.DO_NOTHING, blank=True, null=True) 
    meettime = models.DateTimeField(blank=True, null=True) 
    isreported = models.BooleanField(blank=True, null=True) 
    isscheduled = models.BooleanField(blank=True, null=True) 
    ghichu = models.CharField(max_length=254, blank=True, null=True) 


class Report(models.Model):
    report_id = models.CharField(primary_key=True, max_length=10) 
    code_url = models.CharField(max_length=100, blank=True, null=True) 
    report = models.CharField(max_length=100, blank=True, null=True) 
    cuochop = models.ForeignKey(Cuochop, models.DO_NOTHING, blank=True, null=True)


class Thanhviennhom(models.Model):
    mathamgia = models.CharField(db_column='MaThamGia', primary_key=True, max_length=8) 
    masv = models.ForeignKey(Sinhvien, models.DO_NOTHING, db_column='MaSV', blank=True, null=True) 
    idnhom = models.ForeignKey(Nhom, models.DO_NOTHING, db_column='IdNhom', blank=True, null=True) 