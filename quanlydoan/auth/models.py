from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.utilities import UserAccountManager

# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField( max_length=254, unique= True )
    fullName = models.CharField(max_length=254)
    is_active = models.BooleanField(default= True)
    is_teacher = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']
    
    def get_full_name(self):
        return self.fullName
    
    def get_short_name(self):
        return self.fullName 
    
    def __str__(self):
        return self.email