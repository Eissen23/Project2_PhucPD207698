from django.db import models

from authentication.models import Students
from common.models import Auditable
from teach_subject.models import Teachers


# Create your models here.
# TODO: Should have project data for this group
class StudentGroups(Auditable):
    term = models.PositiveIntegerField( blank=True, null=True)
    group_name = models.CharField( max_length=10, blank=True, null=True)
    lead_teacher = models.ForeignKey(Teachers, models.DO_NOTHING, blank=True, null=True)
    project_title = models.CharField( max_length=255, blank=True, null=True)
    descrition = models.TextField( blank=True, null=True)

class GroupMembers(Auditable):
    student = models.ForeignKey(Students, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(StudentGroups, models.CASCADE, blank=True, null=True)