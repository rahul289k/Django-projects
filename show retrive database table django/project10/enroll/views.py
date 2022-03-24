from django.shortcuts import render
from .models import Students 


def studentinfo(request):
    stud = Students.objects.all()
    return render(request,'enroll/studetails.html',{'stu':stud})


# Create your views here.
