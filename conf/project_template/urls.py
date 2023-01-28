"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
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
"""
import os
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('apps.core.urls'))
]

APPS_DIR = settings.BASE_DIR.joinpath('apps')

# adding app urls..
for app in os.listdir(APPS_DIR):
    if app != 'core' and 'urls.py' in os.listdir(APPS_DIR.joinpath(app)):
        urlpatterns += [
            path(app + '/', include('apps.' + app + '.urls'), name=app)
        ]

if getattr(settings, 'DJDT', False):
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
