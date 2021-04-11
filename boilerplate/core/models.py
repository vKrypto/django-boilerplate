from django.utils.timezone import now
from django.db import models
from jsonfield import JSONField
from django.db.models import Q
from uuid import uuid4
# local imports
from . import JobStatus


# Create your models here.
class JobQuerySet(models.QuerySet):
    def failed(self):
        self.filter(Q(status=JobStatus.FAILED))

    def executed(self):
        self.filter(Q(status=JobStatus.EXECUTED))

    def interrupted(self):
        self.filter(Q(status=JobStatus.INTERRUPTED))

    def running(self):
        self.filter(Q(status=JobStatus.RUNNING))

    def rejected(self):
        self.filter(Q(status=JobStatus.REJECTED))

    def created(self):
        self.filter(Q(status=JobStatus.CREATED))


class Job(models.Model):
    created = models.DateTimeField(default=now, editable=True)
    token = models.CharField(max_length=36, unique=True, default=str(uuid4()))
    status = models.CharField(max_length=32, default=JobStatus.CREATED, choices=JobStatus.CHOICES)

    input_args = JSONField(null=True, blank=True, default={})
    finished_by = models.DateTimeField(null=True, editable=True)

    objects = JobQuerySet.as_manager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def mark_as_finished(self):
        self.finished_by = now()
        self.status = JobStatus.EXECUTED
        self.save()
