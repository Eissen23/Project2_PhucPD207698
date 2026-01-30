from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.enum import TeacherStatus
from authentication.managers import UserAccountManager
from common.models import Auditable

class StudentClasses(Auditable):
    major = models.CharField(max_length=100, blank=True, null=True)
    generation = models.PositiveIntegerField()
    intake_year = models.PositiveIntegerField()
    graduation_year = models.PositiveIntegerField()

class UserAccount(AbstractBaseUser, PermissionsMixin, Auditable):
    email = models.EmailField( max_length=254, unique= True )
    full_name = models.CharField(max_length=254)
    is_active = models.BooleanField(default= True)
    is_teacher = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

# Add foreign key for class(include major) *Not needed rn*
class Students(Auditable):
    phone = models.CharField( max_length=10, blank=True, null=True)
    user_account = models.ForeignKey(UserAccount, models.CASCADE)
    student_class = models.ForeignKey(StudentClasses, models.CASCADE, null=True)

class Teachers(Auditable):
    institute = models.CharField(max_length=100, blank=True, null=True)
    joined_since = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True, choices=TeacherStatus, default=TeacherStatus.ACTIVE)
    user_account = models.ForeignKey(UserAccount, models.CASCADE)
