from django import forms
# from .models import Mess # class


class UserLoginForm(forms.Form):  # Model forms
    # class Meta: #  inner class

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)