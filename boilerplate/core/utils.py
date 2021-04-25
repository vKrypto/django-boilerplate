# global imports
from celery import shared_task
from django.conf import settings
import os
import subprocess
# local imports
from .models import Job

# local variables
TEMPLATE_DIR = settings.BASE_DIR.joinpath('conf')


class Branch:
    PROJECT = 'render_project_architecture'
    RENDER_APPS = 'render_apps'
    DB_SETUP = 'initialize_db'
    OPTIMIZE_CODE = "optimization"


def dump_logs():
    pass


def _create_gitignore():
    """
    create a .gitignore file in final build to avoid venv files
    """
    gitignore = open(".gitignore", "w")
    entries = ["venv"]
    gitignore.write("\n".join(entries))
    gitignore.close()


def switch_dir(dir_path):
    os.chdir(dir_path)


def _bash(job_token: str, shell_command: str, about: str):
    """
    raise error, and stop further processing of job, and keep error logs
    """
    proc = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    job = Job.objects.get(token=job_token)
    job_log = job.logs.create(shell_command=shell_command, output=output, error=error, about=about)
    job_log.dump_log()
    if error:
        raise Exception(error)
    print(about)


# def write_log(file_path, log):
#     """
#     append log in file..
#     """
#     f = open(file_path, "ab")
#     f.write(log)
#     f.close()


def hello():
    print("hello")


def test():
    start_job_execution(Job.objects.first().token)


@shared_task()
def start_job_execution(token: str):
    job = Job.objects.get(token=token)
    switch_dir(job.project_dir)  # step 1: switch into workspace dir
    create_fresh_environment(token)  # step 2: create a fresh environment.
    prepare_environment(token)  # step 3: prepare environment for project.
    initialize_git(token)  # step 4: initialize git to create version control, while developing.
    git_checkout(token, Branch.PROJECT)  # step 5: commit changes and switch branch for project-architecture render
    render_project(token)  # step 6: create project architecture..
    git_checkout(token, Branch.RENDER_APPS)  # step 7: commit changes and switch branch for rendering apps .
    render_core_app(token)  # step 8: render core app.
    render_account_app(token)  # step 9: render account app
    # render_custom_app(token)  # step 9: render custom app
    git_checkout(token, Branch.DB_SETUP)  # step 10: commit changes and switch branch for further process
    run_migrations(token)  # step 11: run migrations, and initialize db
    collect_static(token)  # step 12: collect all static files
    internationalization(token)  # step 13: creating trans messages for project
    system_check(token)  # step 14: running system checks..
    git_checkout(token, Branch.OPTIMIZE_CODE)  # step 15: commit changes and switch branch for further process


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
    # _bash(token, "source venv/bin/activate", "activating virtual environment")  # source not works in os.system()
    _bash(token, "venv/bin/pip install --upgrade pip", "upgrading pip module")
    _bash(token, "venv/bin/pip install " + " ".join(pip_modules), "installing required dependencies")
    _bash(token, "echo '" + "\n".join(pip_modules) + "' > requirements.txt", "writing pip modules.")
    _bash(token, "venv/bin/pip freeze > lock_requirements.txt", "lock pip version")


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
def render_project(token):
    """
    render project conf and settings, create project structure,
    make and run initial migrations,
    set site info objects in models
    """
    shell_cmd = "venv/bin/django-admin startproject project --verbosity 2 --template " + str(
        TEMPLATE_DIR.joinpath('project_template'))
    _bash(token, shell_cmd, "Generating project Architecture")


@shared_task()
def render_core_app(token):
    """
    configure core apps, with customization,
    render frontend  html css bootstrap.
    """
    _bash(token, "mkdir project/apps/core", "creating core folder.")
    shell_cmd = "venv/bin/django-admin startapp core project/apps/core --verbosity 2 --template " + str(
        TEMPLATE_DIR.joinpath('core_template'))
    _bash(token, shell_cmd, "Rendering core app.")


@shared_task()
def render_account_app(token):
    """
    render account app, with user requirements,
    make and run migrations and initialize db with keys if required.
    """
    _bash(token, "mkdir project/apps/accounts", "creating accounts folder.")
    shell_cmd = "venv/bin/django-admin startapp accounts project/apps/accounts --verbosity 2 --template " + str(
        TEMPLATE_DIR.joinpath('account_template'))
    _bash(token, shell_cmd, "Rendering account app.")


@shared_task()
def run_migrations(token):
    """
    delete all apps migrations and,
    regenerate them and migrate as fake.
    """
    bash_command = "venv/bin/python3 project/manage.py"
    _bash(token, bash_command + " makemigrations", "running makemigrations.")
    _bash(token, bash_command + " migrate", "migrating Database.")


@shared_task()
def clean_migrations():
    """
    delete all apps migrations and,
    regenerate them and migrate as fake.
    """
    pass


@shared_task()
def collect_static(token):
    """
    collect static to corresponding storage locations.
    """
    _bash(token, "venv/bin/python3 project/manage.py collectstatic --noinput", "collecting static files.")


@shared_task()
def internationalization(token):
    """
    django trans:
    generate, compile messages for project in different languages.
    """
    base_command = "venv/bin/python3 project/manage.py"
    _bash(token, base_command + " makemessages --ignore venv --all", "generating messages for project.")
    _bash(token, base_command + " compilemessages", "compiling messages for project.")


@shared_task()
def system_check(token):
    """
    perform system_checks, checks that app is running or not.
    """
    _bash(token, "venv/bin/python3 project/manage.py check", "checking system issues.")


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
