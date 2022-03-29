from dataclasses import field
from unittest.util import _MAX_LENGTH
from django import forms
from django.core import validators
from .models import User

class StudenRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']

