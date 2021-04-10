from django.urls import path, include

#local import
from .views import *

urlpatterns = [
    path(r'', home, name='home')
]