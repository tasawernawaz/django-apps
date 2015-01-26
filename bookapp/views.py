__author__ = 'Tasawer Nawaz'

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world")