from django.http import HttpResponse
from django.shortcuts import render
from .utils import hello


# create your views here.
def home(request):
    print(">>>>>>>>")
    hello.delay()
    return HttpResponse("oK")


def deploy_project(request):
    job = Job.objects.create()
    start_job_execution.delay(job.token)
    return HttpResponse("project rendered..")