from distutils.command.clean import clean
from django import forms
from django.core import validators


# building custom validators

class StudentRegistration(forms.Form):


    # biult-in validators
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])  

   
# implementation of custom validation
    name = forms.CharField() 
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    rpassword = forms.CharField(widget = forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valpwv = cleaned_data['password']
        rvalpass = cleaned_data['rpassword']

        if valpwv != rvalpass:
            raise forms.ValidationError("your pw do not match re-enter pw")