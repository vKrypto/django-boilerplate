# global import 
from django.shortcuts import render
from django.views.generic import TemplateView

# local import 
from .models import *
from .forms import *
from .filters import *
from .utils import *
from .serializers import *

""" all views goes here."""


# class HomePagePiew(TemplateView):
#     """ home page """
#     template_name = "home.html"