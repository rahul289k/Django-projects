from django.shortcuts import render
from django.http import HttpResponse

def fees_structure(request):
    a = 300
    return HttpResponse(f"fees of this course is {a} ")

# Create your views here.
