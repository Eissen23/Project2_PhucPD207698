# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cuochop(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idnhom = models.ForeignKey('Nhom', models.DO_NOTHING, db_column='IdNhom', blank=True, null=True)  # Field name made lowercase.
    noteid = models.ForeignKey('Note', models.DO_NOTHING, db_column='NoteId', blank=True, null=True)  # Field name made lowercase.
    meettime = models.DateTimeField(db_column='MeetTime', blank=True, null=True)  # Field name made lowercase.
    isnoted = models.IntegerField(db_column='isNoted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuochop'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Giangvien(models.Model):
    magv = models.CharField(db_column='MaGV', primary_key=True, max_length=5)  # Field name made lowercase.
    hotengb = models.CharField(db_column='HoTenGB', max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    vien = models.CharField(db_column='Vien', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giangvien'


class Mon(models.Model):
    mamon = models.OneToOneField(Giangvien, models.DO_NOTHING, db_column='MaMon', primary_key=True)  # Field name made lowercase. The composite primary key (MaMon, MaGV) found, that is not supported. The first column is selected.
    magv = models.CharField(db_column='MaGV', max_length=5)  # Field name made lowercase.
    tenmon = models.CharField(db_column='TenMon', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mon'
        unique_together = (('mamon', 'magv'),)


class Nhom(models.Model):
    idnhom = models.CharField(db_column='IdNhom', primary_key=True, max_length=5)  # Field name made lowercase.
    mamon = models.ForeignKey(Mon, models.DO_NOTHING, db_column='MaMon', blank=True, null=True)  # Field name made lowercase.
    magv = models.ForeignKey(Giangvien, models.DO_NOTHING, db_column='MaGV', blank=True, null=True)  # Field name made lowercase.
    term = models.PositiveIntegerField(db_column='Term', blank=True, null=True)  # Field name made lowercase.
    tennhom = models.CharField(db_column='TenNhom', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tendetai = models.CharField(db_column='TenDetai', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    projectstatus = models.IntegerField(db_column='ProjectStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhom'


class Note(models.Model):
    noteid = models.CharField(db_column='NoteId', primary_key=True, max_length=10)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'note'


class Sinhvien(models.Model):
    masv = models.CharField(db_column='MaSV', primary_key=True, max_length=6)  # Field name made lowercase.
    hoten = models.CharField(db_column='HoTen', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idnhom = models.ForeignKey(Nhom, models.DO_NOTHING, db_column='IdNhom', blank=True, null=True)  # Field name made lowercase.
    malop = models.CharField(db_column='MaLop', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sdt = models.CharField(db_column='SDT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nganh = models.CharField(db_column='Nganh', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emailsv = models.CharField(db_column='EmailSV', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sinhvien'


# base on the video about React-Django Rest Authenication
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField( max_length=254, unique= True )
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default= True)
    is_teacher = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name 
    
    def __str__(self):
        return self.email
    
class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('User must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        
        user.set_password(password)
        user.save()
        
        return user