from tasks import my_first_task, send_email_task
from django.shortcuts import render
from django.http import HttpResponse


def task(request):
    my_first_task.delay()
    return HttpResponse('Hello world')


def send_email(request):
    send_email_task.delay()
    return render(request, 'index.html')