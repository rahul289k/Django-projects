from django.shortcuts import render,redirect
from .forms import StudentRegistration
from django.http import HttpResponseRedirect


def completed(request):
    return render(request,'enroll/success.html')

def showformdata(request):

    if request.method =='POST':
    
        obj = StudentRegistration(request.POST)
        if obj.is_valid():

            print("this is from post method")
            print(obj) 
            name = obj.cleaned_data['name']
            email= obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            print("Name:",name)
            print("Email:",email)
            print("Password:",password)
            return HttpResponseRedirect('/regi/completed')

        
        # return render(request,'enroll/reg.html',{'form':obj}),redirect('/regi/completed')
            
    else:
        obj = StudentRegistration()
        print("this is from get method")
        return render(request,'enroll/reg.html',{'form':obj})


    # Create your views here.
