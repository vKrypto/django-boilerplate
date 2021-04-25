from django.urls import path, include

#local import
from .views import *

urlpatterns = [
    path(r'', home, name='home')
    path(r'deploy-project', deploy_project, name='deplo-project')
]