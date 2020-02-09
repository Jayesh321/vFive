from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.IntegerField()
    firstname=forms.CharField(max_length=256)
    lastname=forms.CharField(max_length=256)
    class Meta:
        model=User
        fields=['username','email', 'firstname', 'lastname','phone', 'password1', 'password2']

