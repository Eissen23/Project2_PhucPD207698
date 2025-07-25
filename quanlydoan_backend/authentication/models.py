from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField( max_length=254, unique= True )
    fullName = models.CharField(max_length=254)
    is_active = models.BooleanField(default= True)
    is_teacher = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']
    
    def __str__(self):
        return self.email
    
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
