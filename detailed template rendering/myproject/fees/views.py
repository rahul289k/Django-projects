from django.shortcuts import render



def fees_django(request):
    return render(request,'fees/feesone.html')


def fees_python(request):
    return render(request,'fees/feestwo.html')



# Create your views here.
