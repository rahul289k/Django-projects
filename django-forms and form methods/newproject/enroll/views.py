from django.shortcuts import render
from .forms import StudentRegistration

def showformdata(request):
    obj = StudentRegistration()
    return render(request,'enroll/reg.html',{'form':obj})


# Create your views here.
