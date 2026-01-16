import uuid

from django.db import models

from authentication.models import Sinhvien
from common.models import Auditable
from teach_subject.models import Giangvien


# Create your models here.
# TODO: Should have project data for this group
class StudentGroups(Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    term = models.PositiveIntegerField( blank=True, null=True)
    group_name = models.CharField( max_length=10, blank=True, null=True)
    lead_teacher = models.ForeignKey(Giangvien, models.DO_NOTHING, blank=True, null=True)

class GroupMembers(Auditable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    student = models.ForeignKey(Sinhvien, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(StudentGroup, models.DO_NOTHING, blank=True, null=True)