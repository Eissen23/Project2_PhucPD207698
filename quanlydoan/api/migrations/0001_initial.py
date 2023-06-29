# Generated by Django 4.2.1 on 2023-06-23 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Cuochop",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "meettime",
                    models.DateTimeField(blank=True, db_column="MeetTime", null=True),
                ),
                (
                    "isnoted",
                    models.IntegerField(blank=True, db_column="isNoted", null=True),
                ),
            ],
            options={
                "db_table": "cuochop",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Giangvien",
            fields=[
                (
                    "magv",
                    models.CharField(
                        db_column="MaGV",
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "hotengb",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="HoTenGB",
                        max_length=40,
                        null=True,
                    ),
                ),
                (
                    "vien",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="Vien",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="Email",
                        max_length=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "giangvien",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Nhom",
            fields=[
                (
                    "idnhom",
                    models.CharField(
                        db_column="IdNhom",
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "term",
                    models.PositiveIntegerField(
                        blank=True, db_column="Term", null=True
                    ),
                ),
                (
                    "tennhom",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="TenNhom",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "tendetai",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="TenDetai",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "projectstatus",
                    models.IntegerField(
                        blank=True, db_column="ProjectStatus", null=True
                    ),
                ),
            ],
            options={
                "db_table": "nhom",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "noteid",
                    models.CharField(
                        db_column="NoteId",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, db_column="Note", max_length=100, null=True
                    ),
                ),
                (
                    "report",
                    models.CharField(
                        blank=True, db_column="Report", max_length=100, null=True
                    ),
                ),
            ],
            options={
                "db_table": "note",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Sinhvien",
            fields=[
                (
                    "masv",
                    models.CharField(
                        db_column="MaSV",
                        max_length=6,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "hoten",
                    models.CharField(
                        blank=True, db_column="HoTen", max_length=40, null=True
                    ),
                ),
                (
                    "malop",
                    models.CharField(
                        blank=True, db_column="MaLop", max_length=10, null=True
                    ),
                ),
                (
                    "sdt",
                    models.CharField(
                        blank=True, db_column="SDT", max_length=10, null=True
                    ),
                ),
                (
                    "nganh",
                    models.CharField(
                        blank=True, db_column="Nganh", max_length=30, null=True
                    ),
                ),
                (
                    "emailsv",
                    models.CharField(
                        blank=True, db_column="EmailSV", max_length=20, null=True
                    ),
                ),
            ],
            options={
                "db_table": "sinhvien",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Mon",
            fields=[
                (
                    "mamon",
                    models.OneToOneField(
                        db_column="MaMon",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="api.giangvien",
                    ),
                ),
                ("magv", models.CharField(db_column="MaGV", max_length=5)),
                (
                    "tenmon",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb3_general_ci",
                        db_column="TenMon",
                        max_length=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "mon",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=254)),
                ("is_active", models.BooleanField(default=True)),
                ("is_teacher", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]