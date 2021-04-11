from celery import shared_task
from datetime import datetime
from django.conf import settings
from pathlib import Path
import os
import subprocess
# local variables
from .models import Job, JobStatus


def dump_logs():
    pass


def switch_dir(dir_path):
    os.chdir(dir_path)


def _bash(job_token: str, shell_command: str, about: str):
    proc = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    job = Job.objects.get(token=job_token)
    job_log = job.logs.create(shell_command=shell_command, output=output, error=error, about=about)
    job_log.dump_log()


# def write_log(file_path, log):
#     """
#     append log in file..
#     """
#     f = open(file_path, "ab")
#     f.write(log)
#     f.close()


def hello():
    print("hello")


@shared_task()
def start_job_execution(token: str):
    job = Job.objects.get(token=token)
    switch_dir(job.project_dir)
    create_fresh_environment(token)
    prepare_environment(token)


@shared_task()
def create_fresh_environment(token: str):
    """ just prepare a python3 environment """
    _bash(token, "python3 -m venv venv", "Creating fresh virtual environment")


@shared_task()
def prepare_environment(token: str):
    """
     install dependencies as per project requirements,
     freeze pip,
     configure venv conf,
    """
    pip_modules = ['django', 'split-settings', 'django-allauth',
                   'django-debug-toolbar', 'django-templated-email', 'django-redis']
    _bash(token, "source venv/bin/activate", "activating virtual environment")
    _bash(token, "pip install --upgrade pip", "upgrading pip module")
    _bash(token, "pip install " + " ".join(pip_modules), "installing required dependencies")
    _bash(token, "pip freeze > requirements.txt", "lock pip version")


@shared_task()
def initialize_git(token: str):
    """"
    initialize git in order to maintain version control of project
    """
    _bash(token, "git init", "initializing git environment")


@shared_task()
def git_checkout(token, new_branch_name):
    """
    commit all changes and checkout to new branch.
    """
    _bash(token, 'git add . && git commit -a -m "syncing"', "committing all changes")
    _bash(token, "git checkout -b " + str(new_branch_name), "checkout to branch: " + str(new_branch_name))


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


@shared_task()
def git_reinitialize():
    """
    run git clean and initialize again to clean all git history.
    """
    pass
