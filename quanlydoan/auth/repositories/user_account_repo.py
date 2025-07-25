from django.contrib.auth.models import BaseUserManager

from auth.models import UserAccount

class UserAccountRepository(BaseUserManager):
    def __init__(self, user_account= None):
        self.user_account = user_account or UserAccount


    def get_users(self, email):
        try:
            return self.user_account.objects.get()
        except self.user_account.DoesNotExist:
            return None
        
    def get_user_by_id(self, user_id):
        try:
            return self.user_account.objects.get(id=user_id)
        except self.user_account.DoesNotExist:
            return None

    def save_data(self, email, fullName, password = None, is_teacher = False):
        if not email:
            raise ValueError('User must have email address')
        
        email = self.normalize_email(email)
        user = self.user_account(email = email, fullName = fullName, is_teacher = is_teacher)

        user.set_password(password)
        user.save()
        
        return user

    def delete(self, user):
        if isinstance( user, UserAccount):
            user.delete()