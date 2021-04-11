from celery import shared_task
from django.conf import settings
from pathlib import Path
# local variables
from .models import Job, JobStatus
# global variables
JOB_DIR = settings.BASE_DIR.joinpath('jobs')
Path(JOB_DIR).mkdir(parents=True, exist_ok=True)


@shared_task()
def hello():
    print("hello")


@shared_task()
def start_job_execution(job_token):
    job = Job.created().get(token=job_token)


@shared_task()
def create_fresh_environment():
    """ just prepare a python3 environment """
    pass


@shared_task()
def prepare_environment():
    """
     install dependencies as per project requirements,
     freeze pip,
     configure venv conf,
    """
    pass


@shared_task()
def render_project():
    """
    render project conf and settings, create project structure,
    make and run initial migrations,
    set site info objects in models
    """
    pass


@shared_task()
def render_core_app():
    """
    configure core apps, with customization,
    render frontend  html css bootstrap.
    """
    pass


@shared_task()
def render_account_app():
    """
    render account app, with user requirements,
    make and run migrations and initialize db with keys if required.
    """
    pass


@shared_task()
def clean_migrations():
    """
    delete all apps migrations and,
    regenerate them and migrate as fake.
    """
    pass


@shared_task()
def collect_static():
    """
    collect static to corresponding storage locations.
    """
    pass


@shared_task()
def internationalization():
    """
    django trans:
    generate, compile messages for project in different languages.
    """
    pass


@shared_task()
def system_check():
    """
    perform system_checks, checks that app is running or not.
    """


@shared_task()
def optimize_code():
    """
    optimize and beautify code
    """
    pass


@shared_task()
def deployment():
    """
    deploy server to local server or aws
    """
    pass


@shared_task()
def check_run_server():
    """
    execute run-server and kill server,
    """
    pass
