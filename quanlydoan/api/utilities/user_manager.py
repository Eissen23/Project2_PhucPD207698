from django.contrib.auth.models import BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, fullName, password = None):
        if not email:
            raise ValueError('User must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, fullName = fullName)
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_teacher(self, email, fullName, password = None ):
        user = self.create_user(email, fullName, password)
        user.is_teacher = True
        
        user.save()
        
        return user
    def create_superuser(self, email, fullName, password = None ):
        user = self.create_user(email, fullName, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.is_teacher = True
        
        user.save()
        
        return user