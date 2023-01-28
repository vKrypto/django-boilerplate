"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

# for a model: 
    istView(contains filter)
    Detailview
    UpdateView
    DeleteView(modlaForm)
    CreateView

# for a model(api): 
    listView(contains filter)
    UpdateView
    DeleteView(modlaForm)
    CreateView
"""

# gloabl import
from django.urls import path, include
from django.urls import re_path

#local import
from .views import *

urlpatterns = [
    # re_path(r'^$', HomePagePiew.as_view(), name='home'),
]