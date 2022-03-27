from django import forms
from django.core import validators


# building custom validators

def starts_with_s(val):
    if val[0] != 's':
        raise forms.ValidationError("enter a name that starts with s")


class StudentRegistration(forms.Form):


    # biult-in validators
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])  

   
# implementation of custom validation
    name = forms.CharField(validators=[starts_with_s]) 
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
