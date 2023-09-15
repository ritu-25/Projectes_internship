from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class register_form(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username','email']
        widgets ={
           'username': forms.TextInput(attrs={'class':'form-control'}),
           'email': forms.TextInput(attrs={'class':'form-control'})
        }