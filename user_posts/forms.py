from django import forms
from django.contrib.auth.models import User
from .models import User_Posts


class UserPostForm(forms.ModelForm):
    class Meta:
        model = User_Posts
        fields = ('title', 'content', 'image', 'tag', 'published_date')