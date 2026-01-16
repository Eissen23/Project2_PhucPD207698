from django.db import models

class TeacherStatus(models.TextChoices):
    ACTIVE = 'ATV', 'Active'
    INACTIVE = 'INA', 'Inactive'
    ABSENCE = 'ABS', 'Excused Absence'
