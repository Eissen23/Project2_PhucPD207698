from django.db import models

from common.models import Auditable
from group.models import StudentGroups


# Create your models here.
class Meetings(Auditable):
    schedule_date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=254, blank=True, null=True)
    student_group = models.ForeignKey(StudentGroups, models.DO_NOTHING, blank=True, null=True)

class Reports(Auditable):
    cloud_url = models.CharField(max_length=100, blank=True, null=True)
    report = models.TextField(blank=True, null=True)
    meeting = models.ForeignKey(Meetings, models.CASCADE, blank=True, null=True)
