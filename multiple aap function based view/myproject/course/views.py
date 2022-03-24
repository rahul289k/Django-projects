from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
   
    return HttpResponse("Hello welcome to django course  ")



# Create your views here.
def home_page(request):
    return HttpResponse("welcome to home page")
    