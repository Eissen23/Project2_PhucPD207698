from asyncio import Task

from django.contrib.postgres.fields import ArrayField
from django.db import models

from authentication.models import Students
from common.models import Auditable
from group.enums import StudentGroupStatus
from teach_subject.models import TeacherSubjects

def get_default_tags():
    return ["Basic projects"]

# Can also be named as Project.
class StudentGroups(Auditable):
    project_title = models.CharField( max_length=255)
    description = models.TextField( blank=True, null=True)
    term = models.PositiveIntegerField(help_text="The term in which the project started")
    status = models.CharField( max_length=10, choices=StudentGroupStatus, default= StudentGroupStatus.ACTIVE, null=True)
    tags = ArrayField(models.CharField(max_length=100), help_text="Tags of group projects type", default=get_default_tags)
    # Foreign key
    teacher_subject = models.ForeignKey(TeacherSubjects, models.DO_NOTHING, blank=True, null=True)

class GroupMembers(Auditable):
    student = models.ForeignKey(Students, models.DO_NOTHING)
    group = models.ForeignKey(StudentGroups, models.CASCADE)

class ProjectTask(Auditable):
    name = models.CharField( max_length=100)
    description = models.TextField( blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    student_group = models.ForeignKey(StudentGroups, models.DO_NOTHING)
    assignee = models.ForeignKey(Students, models.DO_NOTHING, blank=True, null=True)
    reference_url = models.URLField(blank=True, null=True)