from django.shortcuts import render
from .forms import StudenRegistration
from django.http import HttpResponseRedirect
from .models import User

def showdata(request):
    if request.method == 'POST':
        obj = StudenRegistration(request.POST)
        if obj.is_valid():
            nm = obj.cleaned_data['name']
            em = obj.cleaned_data['email']
            pw = obj.cleaned_data['password']
            reg = User(name = nm,email = em,password = pw)
            reg.save()
            # print(nm)
            # print(em)
            # print(pw)
            # # return HttpResponseRedirect('/regi/msg')

    else: 
        obj = StudenRegistration()

    return render(request,'enroll/userregistration.html', {'form':obj})




# Create your views here.
