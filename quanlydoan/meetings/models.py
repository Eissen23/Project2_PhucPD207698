from django.db import models

from quanlydoan.api.models import Nhom

# Create your models here.
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
