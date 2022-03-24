from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_djnago(request):
    course_name = "django is awesome"
    d = datetime.now()
    price = 650
    additional = 1000-price

    django_details = {'nm':course_name,'dt':d,'p1':56.12340505,'p2':56.00000,'p3':56,'price':price,'more':additional }

    return render(request,'course/courseone.html',django_details)