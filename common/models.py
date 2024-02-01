import uuid
from django.db import models

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class StatefulModel(models.Model):
    ACTIVE = 1
    DRAFT = 0
    DELETED = 9

    STATUS_CHOICES = [
        (ACTIVE, 'Activo'),
        (DRAFT, 'Borrador'),
        (DELETED, 'Borrado')
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    @property
    def is_active(self):
        return self.status == self.ACTIVE

    @property
    def is_draft(self):
        return self.status == self.DRAFT

    @property
    def is_deleted(self):
        return self.status == self.DELETED

    class Meta:
        abstract = True
