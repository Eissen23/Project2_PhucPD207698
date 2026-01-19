from django.db import models

from authentication.models import UserAccount, Teachers
from common.models import Auditable

# TODO: What should i do with this?
class Subjects(Auditable):
    name = models.CharField(max_length=20, blank=True, null=True)

class TeacherSubjects(Auditable):
    subject_id = models.ForeignKey(Subjects, models.DO_NOTHING, blank=True, null=True)
    teacher_id = models.ForeignKey(Teachers, models.DO_NOTHING, blank=True, null=True)
# Enum
