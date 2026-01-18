from django.db import models

from group.models import StudentGroups


# Create your models here.
class Meetings(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    group_id = models.ForeignKey(StudentGroups, models.DO_NOTHING, blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=254, blank=True, null=True)

class Reports(models.Model):
    report_id = models.CharField(primary_key=True, max_length=10)
    code_url = models.CharField(max_length=100, blank=True, null=True) 
    report = models.CharField(max_length=100, blank=True, null=True) 
    meeting_id = models.ForeignKey(Meetings, models.CASCADE, blank=True, null=True)
