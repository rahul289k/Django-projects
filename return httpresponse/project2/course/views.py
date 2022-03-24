
from django.shortcuts import render
from django.http import HttpResponse
def home_page(request):
    return HttpResponse("Hello welcome to Home page ")

def learn_django(request):
    return HttpResponse("Hello  Django")


def learn_python(request):
    return HttpResponse("Hello Python")


def learn_var(request):
    a = '<h1>Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    value = 10+10
    return HttpResponse(value)


def learn_format(request):
    a = "Rahul"
    return HttpResponse(f'hello how are you {a}')
# Create your views here.
