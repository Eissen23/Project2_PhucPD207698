from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.enum import TeacherStatus
from common.models import Auditable

# TODO: There will be problem in the future with save and update method

class UserAccount(AbstractBaseUser, PermissionsMixin, Auditable):
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
class Students(Auditable):
    phone = models.CharField( max_length=10, blank=True, null=True)
    user_id = models.ForeignKey(UserAccount, models.CASCADE)

class Teachers(Auditable):
    institute = models.CharField(max_length=100, blank=True, null=True)
    joined_since = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True, choices=TeacherStatus, default=TeacherStatus.ACTIVE)
    user_id = models.ForeignKey(UserAccount, models.CASCADE)