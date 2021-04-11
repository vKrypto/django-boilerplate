from django.utils.timezone import now
from django.db import models
from django.conf import settings
from jsonfield import JSONField
from pathlib import Path
from django.db.models import Q
from uuid import uuid4
# local imports
from . import JobStatus
# define global variables
JOB_DIR = settings.BASE_DIR.joinpath('jobs')


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

    @property
    def project_dir(self):
        project_dir = JOB_DIR.joinpath(self.token, 'project')
        Path(project_dir).mkdir(parents=True, exist_ok=True)  # make  sure it exists
        return project_dir

    @property
    def project_log_dir(self):
        project_log_dir = JOB_DIR.joinpath(str(self.token), 'logs')
        Path(project_log_dir).mkdir(parents=True, exist_ok=True)  # make  sure it exists
        return project_log_dir

    def mark_as_finished(self):
        self.finished_by = now()
        self.status = JobStatus.EXECUTED
        self.save()


class JobHistory(models.Model):
    job = models.ForeignKey(Job,  related_name='history', on_delete=models.CASCADE)

    method_name = models.CharField(max_length=50)
    input_args = JSONField(null=True, blank=True, default={})

    any_error = models.BooleanField(default=False)  # may required to re-run is any error
    executed = models.BooleanField(default=False)  # mark true if executed successfully.

    def execute_again(self):
        """
        execute step again, and continue process further.
        """
        if self.any_error:
            pass


class JobLogs(models.Model):
    """"
        temp model store for jobs.
    """
    job = models.ForeignKey(Job, related_name='logs', on_delete=models.CASCADE)
    created = models.DateTimeField(default=now)
    shell_command = models.TextField()
    about = models.CharField(max_length=50, default='', blank=True)

    output = models.TextField(null=True, blank=True, default='')
    error = models.TextField(null=True, blank=True, default='')

    is_delivered = models.BooleanField(default=False)
    is_failed = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.error:
            self.is_failed = True
        super().save(*args, **kwargs)

    def dump_log(self):
        """ write log, error log to file system """
        if self.error:
            log_file = str(self.created) + ".error_log"
            file_path = self.job.project_log_dir.joinpath(log_file)
            f = open(file_path, "a+")
            f.write(str(self.error))
            f.close()
        if self.output:
            log_file = str(self.created) + ".log"
            file_path = self.job.project_log_dir.joinpath(log_file)
            f = open(file_path, "a+")
            f.write(str(self.output))
            f.close()
