import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import Auditable
# Create your models here.
# TODO: There will be problem in the future with save and update method
class UserAccount(AbstractBaseUser, PermissionsMixin, Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField( max_length=254, unique= True )
    fullName = models.CharField(max_length=254)
    is_active = models.BooleanField(default= True)
    is_teacher = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']
    
    def __str__(self):
        return self.email

# TODO: Add foreign key for class
# TODO: Add enum for major
class Sinhvien(Auditable):
    student_code = models.CharField(primary_key=True, max_length=8)
    full_name = models.CharField( max_length=40, blank=True, null=True)
    phone = models.CharField( max_length=10, blank=True, null=True)
    user_id = models.ForeignKey(UserAccount, models.CASCADE)
