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

    # username = forms.CharField(
    #     label="Username",
    #     min_length=4,
    #     max_length=20,
    #     widget=forms.TextInput, required=True)
    
    password1 = forms.CharField(
        label="Password",
        min_length=4,
        max_length=20,
        widget=forms.PasswordInput)
             
    password2 = forms.CharField(
        label="Password Confirmation",
        min_length=4,
        max_length=20,
        widget=forms.PasswordInput)

    class Meta:  # inner class provides info about blueprint form
        model = User  # we want to store info in
        fields = ['email', 'username', 'password1', 'password2']


    def clean_email(self):

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
       
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address has to be unique')
      
        return email

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
      
        if password1 != password2:
            raise ValidationError("Passwords have to match")
        
        return password2

    # def clean_input(self):
    #     cleaned_data = super(UserCreationForm, self).clean()
    #     username = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     password1 = cleaned_data.get('password')
    #     if not username and not email and not password1:
    #         raise forms.ValidationError('There are issues with your input')