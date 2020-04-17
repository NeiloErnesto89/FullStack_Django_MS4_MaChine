from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # base for Django 
from django.core.exceptions import ValidationError


# from .models import Mess # class
class UserLoginForm(forms.Form):  # Model forms
    # class Meta: #  inner class

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreationForm(UserCreationForm):  # as arg

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
             
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:  # inner class provides info about blueprint form
        model = User  # we want to store info in
        fields = ['email', 'username', 'password1', 'password2']


    # def clean_input(self):
    #     cleaned_data = super(UserCreationForm, self).clean()
    #     username = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     password1 = cleaned_data.get('password')
    #     if not username and not email and not password1:
    #         raise forms.ValidationError('There are issues with your input')