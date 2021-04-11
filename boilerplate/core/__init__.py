from django.utils.translation import pgettext_lazy as _


class JobStatus:
    CREATED = 'created'
    RUNNING = 'running'
    INTERRUPTED = 'interrupted'
    FAILED = 'failed'
    EXECUTED = 'executed'
    REJECTED = 'rejected'

    CHOICES = [
        (CREATED, _(
            'Status for a job, successfully created',
            'created')),
        (RUNNING, _(
            'Status for a still running jobs',
            'running')),
        (INTERRUPTED, _(
            'Status for a interrupted jobs',
            'interrupted')),
        (RUNNING, _(
            'Status for a job, still running',
            'running')),
        (FAILED, _(
            'Status for a failed jobs',
            'failed')),
        (EXECUTED, _(
            'Status for a job, successfully executed',
            'executed')),
        (REJECTED, _(
            'Status for a rejected jobs',
            'rejected')),
    ]
