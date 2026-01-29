import uuid

from django.conf import settings
from django.db import models

# Create your models here.
class Auditable(models.Model):
    """
    Abstract base class that provides audit fields for tracking
    creation and modification of model instances.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="Timestamp when the record was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text="Timestamp when the record was last updated"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created",
        editable=False,
        help_text="User who created this record"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_updated",
        editable=False,
        help_text="User who last updated this record"
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """
        Override save to handle user tracking.
        Pass 'current_user' in kwargs to set created_by/updated_by.
        """
        current_user = kwargs.pop('current_user', None)

        if current_user and current_user.is_authenticated:
            if not self.pk:  # New instance
                self.created_by = current_user
            self.updated_by = current_user

        # super() will call the next class in MRO (Method Resolution Order)
        # This ensures compatibility with AbstractBaseUser and other mixins
        super().save(*args, **kwargs)

