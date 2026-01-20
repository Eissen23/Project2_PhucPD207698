from  django.db import models

class StudentGroupStatus(models.TextChoices):
    ACTIVE = 'AT', 'Active',
    FINISHED = 'FG', 'Finished',
    DISQUALIFIED = 'DF', 'Disqualified',
