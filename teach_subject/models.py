import uuid

from django.db import models

from authentication.models import UserAccount, Teachers
from common.models import Auditable


class Subjects(Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=20, blank=True, null=True)

class TeacherSubjects(Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    subject_id = models.ForeignKey(Subjects, models.DO_NOTHING, blank=True, null=True)
    teacher_id = models.ForeignKey(Teachers, models.DO_NOTHING, blank=True, null=True)
# Enum
