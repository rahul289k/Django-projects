from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hello Django")


def learn_python(request):
    return HttpResponse("Hello Python")
# Create your views here.
