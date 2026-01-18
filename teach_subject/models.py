import uuid

from django.db import models

from authentication.models import UserAccount
from common.models import Auditable
from meetings.enum import TeacherStatus


class Teachers(Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    institute = models.CharField(max_length=100, blank=True, null=True)
    joined_since = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True, choices=TeacherStatus, default=TeacherStatus.ACTIVE)
    user_id = models.ForeignKey(UserAccount, models.CASCADE)

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
